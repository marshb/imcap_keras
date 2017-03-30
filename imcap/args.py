import argparse

def get_parser():

    parser = argparse.ArgumentParser(description='Image Captioning in Keras',epilog='Good luck!')

    # naming & savefiles
    parser.add_argument('-model_name', dest='model_name',
                        default = 'resnet_cider',help='Base name to save model')
    parser.add_argument('-h5file', dest='h5file',
                        default = 'datasetv2.h5',
                        help='name of hdf5 file (with extension)')
    parser.add_argument('-vfile', dest='vfile',
                        default = 'vocab.pkl',
                        help='name of vocab file (with extension)')
    parser.add_argument('-model_file', dest='model_file',
                        default = 'model_file',help='path to model file to load.')

    # data-related
    parser.add_argument('-num_val',dest='num_val', default = 5000,
                        help='Number of validation images',type=int)
    parser.add_argument('-num_test',dest='num_test', default = 5000,
                        help='Number of test images',type=int)
    parser.add_argument('-coco_path', dest='coco_path',
                        default = '/seq/segmentation/COCO/tools',
                        help='COCO database')
    parser.add_argument('-year', dest='year',
                        default = '2014',help='COCO year')
    parser.add_argument('-data_folder', dest='data_folder',
                        default = '/work/asalvador/sat_keras/',
                        help='save folder')

    # model parts, inputs
    parser.add_argument('-cnn', dest='cnn',
                        default = 'resnet', choices=['vgg16','vgg19','resnet'],
                        help='Pretrained CNN to use')
    parser.add_argument('-resize', dest='resize',
                        default = 256, help='Image resize',type=int)
    parser.add_argument('-imsize', dest='imsize',
                        default = 224, help='Image crop size',type=int)
    parser.add_argument('-vocab_size', dest='vocab_size',
                        default = 10000, help='Vocabulary size' ,type=int)
    parser.add_argument('-n_caps', dest='n_caps',
                        default = 5, help='Number of captions for training',
                        type=int)

    # Model parameters
    parser.add_argument('-seqlen',dest='seqlen', default = 20,
                        help='Maximum sentence length',type=int)
    parser.add_argument('-lstm_dim',dest='lstm_dim', default = 512,
                        help='Number of LSTM units',type=int)
    parser.add_argument('-emb_dim',dest='emb_dim', default = 512,
                        help='Word embedding dim',type=int)
    parser.add_argument('-z_dim',dest='z_dim', default = 512,
                        help='Dimensionality of z space',type=int)
    parser.add_argument('-dr_ratio',dest='dr_ratio', default = 0.5,
                        help='Dropout ratio',type=int)

    # Training params
    parser.add_argument('-seed', dest='seed',
                        default = 4242, help='Random seed',type=int)
    parser.add_argument('-bs',dest='bs', default = 64,
                            help='Batch Size',type=int)
    parser.add_argument('-optim',dest='optim', default ='adam',
                                choices=['adam','SGD','adadelta','adagrad',
                                'rmsprop'], help='Optimizer')
    parser.add_argument('-lr',dest='lr', default = 1e-2,
                                help='Learning rate',type=float)
    parser.add_argument('-ftlr',dest='ftlr', default = 1e-4,
                                help='Learning rate when fine tuning',type=float)
    parser.add_argument('-decay',dest='decay', default = 0.0,
                                help='LR decay',type=float)
    parser.add_argument('-clip',dest='clip', default = 5.0,
                        help='Gradient clipping threshold (value)',type=float)
    parser.add_argument('-nepochs',dest='nepochs', default = 20,
                        help='Number of train epochs (frozen cnn)',type=int)
    parser.add_argument('-ftnepochs',dest='ftnepochs', default = 30,
                        help='Number of train epochs (ft cnn)',type=int)
    parser.add_argument('-pat',dest='pat', default = 5,
                            help='Patience',type=int)
    parser.add_argument('-l2reg',dest='l2reg', default = 1e-8,
                        help='l2 penalty on weights',type=float)
    parser.add_argument('-workers',dest='workers', default = 2,
                        help='Number of data loading threads',type=int)
    parser.add_argument('-es_prev_words',dest='es_prev_words', default = 'gen',
                        help='Previous words to use for early stopping metric computation',
                        choices=['gt','gen'])
    parser.add_argument('-es_metric',dest='es_metric', default = 'CIDEr',
                        help='Early stopping metric',
                        choices=['loss','CIDEr','Bleu_4','Bleu_3','Bleu_2',
                                 'Bleu_1','ROUGE_L','METEOR'])
    # flags & bools
    parser.add_argument('-mode', dest='mode',
                        default = 'train',choices=['train','test'],
                        help='Model mode')
    parser.add_argument('--cnnfreeze', dest='cnn_train', action='store_false')
    parser.add_argument('--cnntrain', dest='cnn_train', action='store_true')
    parser.set_defaults(cnn_train=False)

    parser.add_argument('--attlstm', dest='attlstm', action='store_true')
    parser.add_argument('--lstm', dest='attlstm', action='store_false')
    parser.set_defaults(attlstm=True)

    parser.add_argument('--sgate', dest='sgate', action='store_true')
    parser.add_argument('--nosgate', dest='sgate', action='store_false')
    parser.set_defaults(sgate=False)

    return parser

if __name__ =="__main__":

    parser = get_parser()
    args_dict = parser.parse_args()