"""
https://github.com/Li-Jiajie/BatchAttachmentDownloader

BatchAttachmentDownloader   v1.4.0
邮件附件批量下载
Python 3开发，支持IMAP4与POP3协议

支持多种附件保存模式、筛选模式

使用场景：通过邮箱收作业、调查等，批量下载附件    等

2021.04.23
Jiajie Li
"""

import downloader
import config


if __name__ == '__main__':
    # 服务器连接与邮箱登录
    downloader = downloader.BatchEmail(config.EMAIL_PROTOCOL, config.SERVER_ADDRESS, config.EMAIL_ADDRESS, config.EMAIL_PASSWORD)

    # 选项设置
    downloader.set_save_mode(config.SAVE_MODE)
    downloader.save_path = config.SAVE_PATH
    downloader.date_begin = config.DATE_BEGIN
    downloader.date_end = config.DATE_END
    downloader.time_zone = config.TIME_ZONE
    downloader.from_name = config.FROM_NAME
    downloader.from_address = config.FROM_ADDRESS
    downloader.subject = config.SUBJECT

    # 下载附件
    downloader.download_attachments()
    downloader.close()
