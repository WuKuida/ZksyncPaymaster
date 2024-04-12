EXCEL_PASSWORD = False   # 如果你在Excel中设置了密码 || True/ False
SHUFFLE_WALLETS = True  # 穿插钱包                        || True/ False

TG_BOT_SEND = False                                 # Включить уведомления в тг или нет           || True/ False
TG_TOKEN = ''                                       # API токен тг-бота - создать его можно здесь - https://t.me/BotFather
TG_ID = 0                                           # id твоего телеграмма можно узнать тут       - https://t.me/getmyid_bot

CHAIN_RPC = {
    'ZkSync'  : 'https://mainnet.era.zksync.io',
    'Ethereum': 'https://rpc.ankr.com/eth',
}

MAX_GAS_ETH = 100                 # gas в gwei (смотреть здесь : https://etherscan.io/gastracker)

RETRY = 5                        # Количество попыток при ошибках / фейлах
TIME_DELAY = [200, 250]          # Задержка между МОДУЛЯМИ         [min, max]
TIME_ACCOUNT_DELAY = [200, 300]    # Задержка между АККАУНТАМИ         [min, max]
TIME_DELAY_ERROR = [10, 20]      # 错误延迟/ фейлах[最小，最大]


VALUE_PRESCALE_SWAP = [0.2, 0.3, 5]  # 余额百分比[min, max, round_decimal]
SLIPPAGE = 1  # %

NUMBER_TRANS = [1, 2]   # 圈数(圈=买+卖)



