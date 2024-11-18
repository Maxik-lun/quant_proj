from .preselection import DividendIndexPreSelection
from skfolio import RiskMeasure
from skfolio.optimization import MeanRisk, ObjectiveFunction
from skfolio.uncertainty_set import EmpiricalMuUncertaintySet
from sklearn.pipeline import Pipeline

def build_robust_cdar(returns, universe_mask, div_yield):
    model = Pipeline(
        [
            ("pre_selection", DividendIndexPreSelection(returns, universe_mask, div_yield, pct_to_keep=0.5)),
            ("optimization", MeanRisk(
                risk_measure=RiskMeasure.CDAR,
                objective_function=ObjectiveFunction.MAXIMIZE_UTILITY, risk_aversion=0.01,
                mu_uncertainty_set_estimator=EmpiricalMuUncertaintySet(confidence_level=0.9)
            )),
        ]
    )
    return model

def build_cdar_ratio(returns, universe_mask, div_yield):
    model = Pipeline(
        [
            ("pre_selection", DividendIndexPreSelection(returns, universe_mask, div_yield, pct_to_keep=0.5)),
            ("optimization", MeanRisk(
                risk_measure=RiskMeasure.CDAR,
                objective_function=ObjectiveFunction.MAXIMIZE_RATIO,
                max_weights=0.2, l2_coef=0.001
            ))
        ]
    )
    return model