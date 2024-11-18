# python -m grpc_tools.protoc --proto_path=./grpc_proto/tinvest/ --python_out=./tinvest --
# PROTO_DIR = protos/tinkoff/invest/grpc
# PACKAGE_PROTO_DIR = tinkoff/invest/grpc
# OUT = .
# PROTOS = protos
rm -r ./tinvest/grpc
# mkdir ./tinvest/grpc
python -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. \
 protos/tinvest/grpc/google/api/*.proto
python -m grpc_tools.protoc -Iprotos --python_out=. --pyi_out=. --grpc_python_out=. \
 protos/tinvest/grpc/*.proto
touch tinvest/grpc/__init__.py
