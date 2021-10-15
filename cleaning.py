from TikTokApi import TikTokApi
import pandas as pd
verify_fp = "verify_kurtmtqx_RiutnvEZ_yfyb_4Swy_Bnsk_ApqSUjSCIlw"
api = TikTokApi.get_instance(custom_verifyFp=verify_fp)

count = 2000

tiktoks = api.by_username("posindonesia_official",count=10)


print(dict(tiktoks))
