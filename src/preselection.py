import numpy as np
import pandas as pd
import numpy.typing as npt
import sklearn.base as skb
import sklearn.feature_selection as skf
import sklearn.utils.validation as skv

class DropNotInIndex(skf.SelectorMixin, skb.BaseEstimator):
    """Transformer for dropping assets not included in the index.

    Parameters
    ----------
    universe_mask : pd.DataFrame of shape (n_dates, n_assets)
        Universe mask

    Attributes
    ----------
    to_keep_ : ndarray of shape (n_assets, )
        Boolean array indicating which assets are remaining.

    n_features_in_ : int
        Number of assets seen during `fit`.

    feature_names_in_ : ndarray of shape (`n_features_in_`,)
        Names of assets seen during `fit`. Defined only when `X`
        has assets names that are all strings.
    """

    to_keep_: np.ndarray

    def __init__(self, universe_mask: pd.DataFrame, returns: pd.DataFrame):
        self.universe_mask = universe_mask
        self.returns = returns

    def fit(self, X: npt.ArrayLike, y=None):
        """Run the correlation transformer and get the appropriate assets.

        Parameters
        ----------
        X : array-like of shape (n_observations, n_assets)
            Price returns of the assets.

        y : Ignored
            Not used, present for API consistency by convention.

        Returns
        -------
        self : DropCorrelated
            Fitted estimator.
        """
        X = self._validate_data(X)
        dates = (self.returns.subtract(X[-1]) == 0).all(axis=1)
        current_date = dates[dates].index[0]
        assets_in_universe = self.universe_mask.loc[:current_date].iloc[-1].astype(bool)
        self.to_keep_ = assets_in_universe.values
        return self

    def _get_support_mask(self):
        skv.check_is_fitted(self)
        return self.to_keep_

class DividendIndexPreSelection(skf.SelectorMixin, skb.BaseEstimator):
    to_keep_: np.ndarray

    def __init__(self, returns: pd.DataFrame, universe_mask: pd.DataFrame, 
                 dividends: pd.DataFrame, pct_to_keep: float = 0.5):
        self.returns = returns
        self.universe_mask = universe_mask
        self.dividends = dividends
        self.pct_to_keep = pct_to_keep

    def fit(self, X, y=None):
        """
        dividends are accumulated
        """
        # Validate and convert X to a NumPy array
        X = self._validate_data(X)
        # Check parameters
        if not 0 < self.pct_to_keep <= 1:
            raise ValueError(
                "`pct_to_keep` must be between 0 and 1"
            )
        n_assets = X.shape[1]
        dates = (self.returns.subtract(X[-1]) == 0).all(axis=1)
        current_date = dates[dates].index[0]
        assets_in_universe = self.universe_mask.loc[:current_date].iloc[-1].astype(bool)
        # Select the top `pct_to_keep` assets with the highest dividends
        div_values = self.dividends.loc[:current_date].sum(axis = 0)
        div_quantile = div_values[assets_in_universe].quantile(1 - self.pct_to_keep)
        self.to_keep_ = (assets_in_universe & (div_values >= div_quantile)).values
        return self

    def _get_support_mask(self):
        skv.check_is_fitted(self)
        return self.to_keep_
    
