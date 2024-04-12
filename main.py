from sys import stdout
from modules import *
from settings import *


logger.remove()
logger.add("./data/log.txt")
logger.add(stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <7}</level> | <cyan>{message}</cyan>")
web3_eth = Web3(Web3.HTTPProvider(CHAIN_RPC['Ethereum'], request_kwargs={'timeout': 60}))


class Worker:

    @staticmethod
    def remove_crlf(input_string):
        return input_string.replace("\r", "").replace("\n", "")

    def work(self):
        i = 0
        for number, key in keys_list:
            str_number = f'{number} / {all_wallets}'
            self.remove_crlf(key)

            i += 1
            address = web3_eth.eth.account.from_key(key).address
            logger.info(f'Account #{i} || {address}\n')

            dexs = [
                SynkSwap,
                # Velocore, # linea上的defi
                # Mute # zks上的另一个defi
            ]
            number_trans = random.randint(NUMBER_TRANS[0], NUMBER_TRANS[1])
            logger.info(f'交易轮次 - {number_trans}\n')
            dex = random.choice(dexs)(key, str_number)
            for _ in range(number_trans):
                token = dex.buy_token()
                sleeping(TIME_DELAY[0], TIME_DELAY[1])
                dex.sold_token(token)
                sleeping(TIME_DELAY[0], TIME_DELAY[1])

            logger.success(f'Account completed, sleep and move on to the next one\n')
            sleeping(TIME_ACCOUNT_DELAY[0], TIME_ACCOUNT_DELAY[1])


if __name__ == '__main__':
    print("官方跨连桥 https://portal.zksync.io/bridge/ 建议跨一次，手续费10u左右")
    print("空投模拟器： https://wenser.xyz/check/zksync")
    print("dune数据看板： https://dune.com/teo/zksync-airdrop-ranking")
    print("交互协议看板： https://zk-flow.net/#/wallet/zkSync")
    print("其他类似看板： https://zksync.netlify.app/zksync/  https://10kx.com/10kData/detail")
    list1 = get_accounts_data()
    all_wallets = len(list1)
    logger.info(f'Number of wallets: {all_wallets}\n')
    keys_list = shuffle(list1)
    worker = Worker()
    worker.work()
