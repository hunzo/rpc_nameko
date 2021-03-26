from nameko.standalone.rpc import ClusterRpcProxy

config = {
    # 'AMQP_URI': AMQP_URI  # e.g. "pyamqp://guest:guest@localhost"
    'AMQP_URI': 'amqp://guest:guest@localhost:5672'
}

with ClusterRpcProxy(config) as cluster_rpc:
    cluster_rpc.service_x.remote_method("hellø")  # "hellø-x-y"
