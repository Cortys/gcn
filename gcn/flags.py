class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

FLAGS = AttrDict(
    dataset = 'cora',
    model = 'gcn',
    learning_rate = 0.001,
    epochs = 200,
    hidden1 = 16,
    dropout = 0.5,
    weight_decay = 5e-4,
    early_stopping = 10,
    max_degree = 3
)
