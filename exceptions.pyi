# Stubs for ssh2.exceptions (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

class AgentAuthenticationError(AuthenticationError): ...

class AgentConnectionError(AgentError): ...

class AgentError(SSH2Error): ...

class AgentGetIdentityError(AgentError): ...

class AgentListIdentitiesError(AgentError): ...

class AgentProtocolError(SSH2Error): ...

class AuthenticationError(SSH2Error): ...

class BadSocketError(SSH2Error): ...

class BadUseError(SSH2Error): ...

class BannerRecvError(SessionError): ...

class BannerSendError(SessionError): ...

class BufferTooSmallError(SSH2Error): ...

class ChannelClosedError(ChannelError): ...

class ChannelEOFSentError(ChannelError): ...

class ChannelError(SSH2Error): ...

class ChannelFailure(ChannelError): ...

class ChannelOutOfOrderError(ChannelError): ...

class ChannelPacketExceeded(ChannelError): ...

class ChannelRequestDenied(ChannelError): ...

class ChannelUnknownError(ChannelError): ...

class ChannelWindowExceeded(ChannelError): ...

class CompressError(SessionError): ...

class DecryptError(SessionError): ...

class EncryptError(SessionError): ...

class FileError(SSH2Error): ...

class HostkeyInitError(SessionError): ...

class HostkeySignError(SessionError): ...

class InvalidPollTypeError(SSH2Error): ...

class InvalidRequestError(SSH2Error): ...

class KeyExchangeError(SessionError): ...

class KnownHostAddError(KnownHostError): ...

class KnownHostCheckError(KnownHostError): ...

class KnownHostCheckFailure(KnownHostCheckError): ...

class KnownHostCheckMisMatchError(KnownHostCheckError): ...

class KnownHostCheckNotFoundError(KnownHostCheckError): ...

class KnownHostDeleteError(KnownHostError): ...

class KnownHostError(SSH2Error): ...

class KnownHostGetError(KnownHostError): ...

class KnownHostReadFileError(KnownHostError): ...

class KnownHostReadLineError(KnownHostError): ...

class KnownHostWriteFileError(KnownHostError): ...

class KnownHostWriteLineError(KnownHostError): ...

class MethodNoneError(SSH2Error): ...

class MethodNotSupported(SessionError): ...

class OutOfBoundaryError(SSH2Error): ...

class PasswordExpiredError(AuthenticationError): ...

class ProtocolError(SSH2Error): ...

class PublicKeyError(SSH2Error): ...

class PublicKeyInitError(PublicKeyError): ...

class PublicKeyProtocolError(SSH2Error): ...

class PublickeyUnverifiedError(AuthenticationError): ...

class RequestDeniedError(SessionError): ...

class SCPProtocolError(SessionError): ...

class SFTPError(SSH2Error): ...

class SFTPHandleError(SFTPError): ...

class SFTPProtocolError(SFTPError): ...

class SSH2Error(Exception): ...

class SessionError(SSH2Error): ...

class SessionHandshakeError(SessionError): ...

class SessionHostKeyError(SessionError): ...

class SessionStartupError(SessionError): ...

class SocketDisconnectError(SSH2Error): ...

class SocketRecvError(SSH2Error): ...

class SocketSendError(SSH2Error): ...

class SocketTimeout(SessionError): ...

class Timeout(SessionError): ...

class UnknownError(SSH2Error): ...

class ZlibError(SessionError): ...