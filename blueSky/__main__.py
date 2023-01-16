from argparse import ArgumentParser

argparser = ArgumentParser(
    prog="StockHist",
    description="Historico de ações no seu terminal"
)

required = argparser.add_argument_group('argumentos requiridos')

required.add_argument('-a', '--acao',
    required=True,
    dest='stock_code',
    help=('Código da ação para consulta na corretora'))

argparser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

args = argparser.parse_args()

print(args.stock_code)