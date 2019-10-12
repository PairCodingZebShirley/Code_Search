import argparse


parser = argparse.ArgumentParser("Train and Test Code Search(Embedding) Model")
parser.add_argument('--model', type=str, default='JointEmbeder', help='model name')
parser.add_argument("--mode", choices=["train", "eval", "repr_code", "search"], default='train',
                    help="The mode to run. The `train` mode trains a model;"
                         " the `eval` mode evaluat models in a test set "
                         " The `repr_code/repr_desc` mode computes vectors"
                         " for a code snippet or a natural language description with a trained model.")
# parser.add_argument('--gpu_id', type=int, default=0, help='GPU ID')
parser.add_argument("--verbose", action="store_true", default=True, help="Be verbose")
parser.add_argument("--debug", default=False, action="store_true",
                    help="enable debug mode to see the hidden variable results")