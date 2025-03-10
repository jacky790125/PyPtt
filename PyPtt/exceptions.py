from . import data_type
from . import i18n


class Error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class UnknownError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class RequireLogin(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class NoPermission(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class LoginError(Exception):
    def __init__(self):
        self.message = i18n.login_fail

    def __str__(self):
        return self.message


class NoFastComment(Exception):
    def __init__(self):
        self.message = i18n.no_fast_comment

    def __str__(self):
        return self.message


class NoSuchUser(Exception):
    def __init__(self, user):
        self.message = i18n.no_such_user + ': ' + user

    def __str__(self):
        return self.message


class UserOffline(Exception):
    def __init__(self, user):
        self.message = i18n.user_offline + ': ' + user

    def __str__(self):
        return self.message


class ParseError(Exception):
    def __init__(self, screen):
        self.message = screen

    def __str__(self):
        return self.message


class NoMoney(Exception):
    def __init__(self):
        self.message = i18n.no_money

    def __str__(self):
        return self.message


class MoneyTooFew(Exception):
    def __init__(self):
        self.message = i18n.money_too_few

    def __str__(self):
        return self.message


class NoSuchBoard(Exception):
    def __init__(self, config, board):
        if config.host == data_type.HOST.PTT1:
            self.message = [
                i18n.PTT,
                i18n.no_such_board
            ]
        else:
            self.message = [
                i18n.PTT2,
                i18n.no_such_board
            ]

        if config.language == data_type.Language.MANDARIN:
            self.message = ''.join(self.message) + ': ' + board
        else:
            self.message = ' '.join(self.message) + ': ' + board

    def __str__(self):
        return self.message


class ConnectionClosed(Exception):
    def __init__(self):
        self.message = i18n.connection_closed

    def __str__(self):
        return self.message


class UnregisteredUser(Exception):
    def __init__(self, api_name):
        self.message = i18n.unregistered_user_cant_use_this_api + ': ' + api_name

    def __str__(self):
        return self.message


class MultiThreadOperated(Exception):
    def __init__(self):
        self.message = i18n.multi_thread_operate

    def __str__(self):
        return self.message


class WrongIDorPassword(Exception):
    def __init__(self):
        self.message = i18n.wrong_id_pw

    def __str__(self):
        return self.message


class WrongPassword(Exception):
    def __init__(self):
        self.message = i18n.error_pw

    def __str__(self):
        return self.message


class LoginTooOften(Exception):
    def __init__(self):
        self.message = i18n.login_too_often

    def __str__(self):
        return self.message


class use_too_many_resources(Exception):
    def __init__(self):
        self.message = i18n.use_too_many_resources

    def __str__(self):
        return self.message


class HostNotSupport(Exception):
    def __init__(self, api):
        self.message = f'{i18n.ptt2_not_support}: {api}'

    def __str__(self):
        return self.message


class NoPush(Exception):
    def __init__(self):
        self.message = i18n.no_comment

    def __str__(self):
        return self.message


class CantResponse(Exception):
    def __init__(self):
        self.message = i18n.no_response

    def __str__(self):
        return self.message


class NeedModeratorPermission(Exception):
    def __init__(self, board):
        self.message = f'{i18n.need_moderator_permission}: {board}'

    def __str__(self):
        return self.message


class ConnectError(Exception):
    def __init__(self, config):
        self.message = i18n.connect_fail

    def __str__(self):
        return self.message


class NoMatchTargetError(Exception):
    def __init__(self, screen_queue: list):
        self.ScreenQueue = screen_queue

    def __str__(self):
        screens = ('\n' + '-' * 50 + '\n').join(self.ScreenQueue.get(3))
        return screens + '\n' + i18n.screen_no_match_target


class NoSuchPost(Exception):
    def __init__(self, board, aid):
        self.message = i18n.replace(
            i18n.no_such_post,
            board,
            aid)

    def __str__(self):
        return self.message


class CanNotUseSearchPostCode(Exception):
    def __init__(self):
        self.message = i18n.can_not_use_search_post_code_f

    def __str__(self):
        return self.message


class UserHasPreviouslyBeenBanned(Exception):
    def __init__(self):
        self.message = i18n.user_has_previously_been_banned

    def __str__(self):
        return self.message


class MailboxFull(Exception):
    def __init__(self):
        self.message = i18n.mail_box_full

    def __str__(self):
        return self.message


class Timeout(Exception):
    def __init__(self):
        self.message = i18n.timeout

    def __str__(self):
        return self.message


class NoSearchResult(Exception):
    def __init__(self):
        self.message = i18n.no_search_result

    def __str__(self):
        return self.message


# 此帳號已設定為只能使用安全連線

class OnlySecureConnection(Exception):
    def __init__(self):
        self.message = i18n.only_secure_connection

    def __str__(self):
        return self.message


class DeletedPost(Exception):
    def __init__(self, board, aid):
        self.message = i18n.replace(
            i18n.deleted_post,
            board,
            aid)

    def __str__(self):
        return self.message


class SetConnectMailFirst(Exception):
    def __init__(self):
        self.message = i18n.set_connect_mail_first

    def __str__(self):
        return self.message

# class SystemOverload(Exception):
#     def __init__(self):
#         self.message = i18n.system_busy_try_later
#
#     def __str__(self):
#         return self.message
