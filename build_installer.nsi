############################################################################################
#      NSIS Installation Script created by NSIS Quick Setup Script Generator v1.09.18
#               Entirely Edited with NullSoft Scriptable Installation System
#              by Vlasis K. Barkas aka Red Wine red_wine@freemail.gr Sep 2006
############################################################################################

!define APP_NAME "Cuppa"
!define COMP_NAME "RS Development"
!define WEB_SITE "http://cuppa.mage.me.uk"
!define VERSION "0.1.0.0"
!define COPYRIGHT "© 2022"
!define DESCRIPTION "Pusing and pulling so you don't have to."
!define LICENSE_TXT "C:\Users\vivi\Desktop\COPYING.txt"
!define INSTALLER_NAME "C:\Users\vivi\Downloads\Nsisqssg\Output\Cuppa\cuppa-0.1-setup.exe"
!define MAIN_APP_EXE "cuppa.exe"
!define INSTALL_TYPE "SetShellVarContext all"
!define REG_ROOT "HKLM"
!define REG_APP_PATH "Software\Microsoft\Windows\CurrentVersion\App Paths\${MAIN_APP_EXE}"
!define UNINSTALL_PATH "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"

######################################################################

VIProductVersion  "${VERSION}"
VIAddVersionKey "ProductName"  "${APP_NAME}"
VIAddVersionKey "CompanyName"  "${COMP_NAME}"
VIAddVersionKey "LegalCopyright"  "${COPYRIGHT}"
VIAddVersionKey "FileDescription"  "${DESCRIPTION}"
VIAddVersionKey "FileVersion"  "${VERSION}"

######################################################################

SetCompressor ZLIB
Name "${APP_NAME}"
Caption "${APP_NAME}"
OutFile "${INSTALLER_NAME}"
BrandingText "${APP_NAME}"
XPStyle on
InstallDirRegKey "${REG_ROOT}" "${REG_APP_PATH}" ""
InstallDir "$PROGRAMFILES\Cuppa"

######################################################################

!include "MUI.nsh"

!define MUI_ABORTWARNING
!define MUI_UNABORTWARNING

!insertmacro MUI_PAGE_WELCOME

!ifdef LICENSE_TXT
!insertmacro MUI_PAGE_LICENSE "${LICENSE_TXT}"
!endif

!insertmacro MUI_PAGE_DIRECTORY

!ifdef REG_START_MENU
!define MUI_STARTMENUPAGE_NODISABLE
!define MUI_STARTMENUPAGE_DEFAULTFOLDER "Cuppa"
!define MUI_STARTMENUPAGE_REGISTRY_ROOT "${REG_ROOT}"
!define MUI_STARTMENUPAGE_REGISTRY_KEY "${UNINSTALL_PATH}"
!define MUI_STARTMENUPAGE_REGISTRY_VALUENAME "${REG_START_MENU}"
!insertmacro MUI_PAGE_STARTMENU Application $SM_Folder
!endif

!insertmacro MUI_PAGE_INSTFILES

!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM

!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_UNPAGE_FINISH

!insertmacro MUI_LANGUAGE "English"

######################################################################

Section -MainProgram
${INSTALL_TYPE}
SetOverwrite ifnewer
SetOutPath "$INSTDIR"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-console-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-datetime-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-debug-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-errorhandling-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-file-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-file-l1-2-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-file-l2-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-handle-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-heap-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-interlocked-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-libraryloader-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-localization-l1-2-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-memory-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-namedpipe-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-processenvironment-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-processthreads-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-processthreads-l1-1-1.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-profile-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-rtlsupport-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-string-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-synch-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-synch-l1-2-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-sysinfo-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-timezone-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-core-util-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-conio-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-convert-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-environment-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-filesystem-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-heap-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-locale-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-math-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-process-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-runtime-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-stdio-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-string-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-time-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\api-ms-win-crt-utility-l1-1-0.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\base_library.zip"
File "C:\Users\vivi\Desktop\cuppa\dist\main\libcrypto-1_1.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\libffi-7.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\libssl-1_1.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cuppa.exe"
File "C:\Users\vivi\Desktop\cuppa\dist\main\pyexpat.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\python3.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\python310.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\select.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\ucrtbase.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\unicodedata.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\VCRUNTIME140.dll"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_asyncio.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_bz2.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_cffi_backend.cp310-win_amd64.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_ctypes.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_decimal.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_hashlib.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_lzma.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_multiprocessing.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_overlapped.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_queue.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_socket.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\_ssl.pyd"
SetOutPath "$INSTDIR\nacl"
File "C:\Users\vivi\Desktop\cuppa\dist\main\nacl\py.typed"
File "C:\Users\vivi\Desktop\cuppa\dist\main\nacl\_sodium.pyd"
SetOutPath "$INSTDIR\cryptography-37.0.2.dist-info"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\INSTALLER"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\LICENSE"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\LICENSE.APACHE"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\LICENSE.BSD"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\LICENSE.PSF"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\METADATA"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\RECORD"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\top_level.txt"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography-37.0.2.dist-info\WHEEL"
SetOutPath "$INSTDIR\cryptography\hazmat\bindings"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography\hazmat\bindings\_openssl.pyd"
File "C:\Users\vivi\Desktop\cuppa\dist\main\cryptography\hazmat\bindings\_rust.pyd"
SetOutPath "$INSTDIR\bcrypt"
File "C:\Users\vivi\Desktop\cuppa\dist\main\bcrypt\_bcrypt.pyd"
SectionEnd

######################################################################

Section -Icons_Reg
SetOutPath "$INSTDIR"
WriteUninstaller "$INSTDIR\uninstall.exe"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_WRITE_BEGIN Application
CreateDirectory "$SMPROGRAMS\$SM_Folder"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!insertmacro MUI_STARTMENU_WRITE_END
!endif

!ifndef REG_START_MENU
CreateDirectory "$SMPROGRAMS\Cuppa"
CreateShortCut "$SMPROGRAMS\Cuppa\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$DESKTOP\${APP_NAME}.lnk" "$INSTDIR\${MAIN_APP_EXE}"
CreateShortCut "$SMPROGRAMS\Cuppa\Uninstall ${APP_NAME}.lnk" "$INSTDIR\uninstall.exe"

!ifdef WEB_SITE
WriteIniStr "$INSTDIR\${APP_NAME} website.url" "InternetShortcut" "URL" "${WEB_SITE}"
CreateShortCut "$SMPROGRAMS\Cuppa\${APP_NAME} Website.lnk" "$INSTDIR\${APP_NAME} website.url"
!endif
!endif

WriteRegStr ${REG_ROOT} "${REG_APP_PATH}" "" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayName" "${APP_NAME}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "UninstallString" "$INSTDIR\uninstall.exe"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayIcon" "$INSTDIR\${MAIN_APP_EXE}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "DisplayVersion" "${VERSION}"
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "Publisher" "${COMP_NAME}"

!ifdef WEB_SITE
WriteRegStr ${REG_ROOT} "${UNINSTALL_PATH}"  "URLInfoAbout" "${WEB_SITE}"
!endif
SectionEnd

######################################################################

Section Uninstall
${INSTALL_TYPE}
Delete "$INSTDIR\api-ms-win-core-console-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-datetime-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-debug-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-errorhandling-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-file-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-file-l1-2-0.dll"
Delete "$INSTDIR\api-ms-win-core-file-l2-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-handle-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-heap-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-interlocked-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-libraryloader-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-localization-l1-2-0.dll"
Delete "$INSTDIR\api-ms-win-core-memory-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-namedpipe-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-processenvironment-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-processthreads-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-processthreads-l1-1-1.dll"
Delete "$INSTDIR\api-ms-win-core-profile-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-rtlsupport-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-string-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-synch-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-synch-l1-2-0.dll"
Delete "$INSTDIR\api-ms-win-core-sysinfo-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-timezone-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-core-util-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-conio-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-convert-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-environment-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-filesystem-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-heap-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-locale-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-math-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-process-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-runtime-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-stdio-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-string-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-time-l1-1-0.dll"
Delete "$INSTDIR\api-ms-win-crt-utility-l1-1-0.dll"
Delete "$INSTDIR\base_library.zip"
Delete "$INSTDIR\libcrypto-1_1.dll"
Delete "$INSTDIR\libffi-7.dll"
Delete "$INSTDIR\libssl-1_1.dll"
Delete "$INSTDIR\cuppa.exe"
Delete "$INSTDIR\pyexpat.pyd"
Delete "$INSTDIR\python3.dll"
Delete "$INSTDIR\python310.dll"
Delete "$INSTDIR\select.pyd"
Delete "$INSTDIR\ucrtbase.dll"
Delete "$INSTDIR\unicodedata.pyd"
Delete "$INSTDIR\VCRUNTIME140.dll"
Delete "$INSTDIR\_asyncio.pyd"
Delete "$INSTDIR\_bz2.pyd"
Delete "$INSTDIR\_cffi_backend.cp310-win_amd64.pyd"
Delete "$INSTDIR\_ctypes.pyd"
Delete "$INSTDIR\_decimal.pyd"
Delete "$INSTDIR\_hashlib.pyd"
Delete "$INSTDIR\_lzma.pyd"
Delete "$INSTDIR\_multiprocessing.pyd"
Delete "$INSTDIR\_overlapped.pyd"
Delete "$INSTDIR\_queue.pyd"
Delete "$INSTDIR\_socket.pyd"
Delete "$INSTDIR\_ssl.pyd"
Delete "$INSTDIR\nacl\py.typed"
Delete "$INSTDIR\nacl\_sodium.pyd"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\INSTALLER"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\LICENSE"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\LICENSE.APACHE"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\LICENSE.BSD"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\LICENSE.PSF"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\METADATA"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\RECORD"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\top_level.txt"
Delete "$INSTDIR\cryptography-37.0.2.dist-info\WHEEL"
Delete "$INSTDIR\cryptography\hazmat\bindings\_openssl.pyd"
Delete "$INSTDIR\cryptography\hazmat\bindings\_rust.pyd"
Delete "$INSTDIR\bcrypt\_bcrypt.pyd"

RmDir "$INSTDIR\bcrypt"
RmDir "$INSTDIR\cryptography\hazmat\bindings"
RmDir "$INSTDIR\cryptography-37.0.2.dist-info"
RmDir "$INSTDIR\nacl"

Delete "$INSTDIR\uninstall.exe"
!ifdef WEB_SITE
Delete "$INSTDIR\${APP_NAME} website.url"
!endif

RmDir "$INSTDIR"

!ifdef REG_START_MENU
!insertmacro MUI_STARTMENU_GETFOLDER "Application" $SM_Folder
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\$SM_Folder\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\$SM_Folder\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\$SM_Folder"
!endif

!ifndef REG_START_MENU
Delete "$SMPROGRAMS\Cuppa\${APP_NAME}.lnk"
Delete "$SMPROGRAMS\Cuppa\Uninstall ${APP_NAME}.lnk"
!ifdef WEB_SITE
Delete "$SMPROGRAMS\Cuppa\${APP_NAME} Website.lnk"
!endif
Delete "$DESKTOP\${APP_NAME}.lnk"

RmDir "$SMPROGRAMS\Cuppa"
!endif

DeleteRegKey ${REG_ROOT} "${REG_APP_PATH}"
DeleteRegKey ${REG_ROOT} "${UNINSTALL_PATH}"
SectionEnd

######################################################################

