# ************************请设置以下参数************************

# 邮箱地址  （必填）
EMAIL_ADDRESS = '*****your email address*****'
# 邮箱密码  （必填）
EMAIL_PASSWORD = '*****your email password*****'

# 邮件协议  （必填，POP3或IMAP4）
EMAIL_PROTOCOL = 'POP3'
# 服务器地址(SSL)    （必填，请根据协议填入合适的地址）
SERVER_ADDRESS = 'pop.qq.com'

# 附件保存位置
#windows 路径示例
SAVE_PATH = r'F:\Email-Attachments'
#macOS 路径示例
# SAVE_PATH = r'/Users/xxx/Downloads'

# 筛选起止时间    yyyy-MM-dd HH:mm:ss
DATE_BEGIN, DATE_END = '2020-10-20 00:00', '2020-11-5 18:00'  # 筛选起止时间（包含此时间）
# 时区 默认东八区北京时间，如需更改请按如下格式更改
TIME_ZONE = '+0800'
# 筛选包含此内容的邮件地址，''表示全部邮件地址
FROM_ADDRESS = ''
# 筛选包含此内容的发件人昵称，''表示全部发件人昵称
FROM_NAME = ''
# 筛选包含此内容的邮件主题，''表示全部邮件主题
SUBJECT = ''
"""
    保存模式    SAVE_MODE
【0：所有附件存入一个文件夹】
【1：每个邮箱地址一个文件夹】
【2：每个邮件主题一个文件夹】
【3：每个发件人的每个邮件主题一个文件夹】
【4：每个发件人昵称一个文件夹】
"""
SAVE_MODE = 1

# ************************请设置以上参数************************
