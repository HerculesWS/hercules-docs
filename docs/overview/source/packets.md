__NOTOC__

==0x64==
 struct PACKET_CA_LOGIN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Version
  /* this+0x6 */ unsigned char ID[24]
  /* this+0x1e */ unsigned char Passwd[24]
  /* this+0x36 */ unsigned char clienttype
 }

==0x65==
 struct PACKET_CH_ENTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int AuthCode
  /* this+0xa */ unsigned long userLevel
  /* this+0xe */ unsigned short clientType
  /* this+0x10 */ unsigned char Sex
 }

==0x66==
 struct PACKET_CH_SELECT_CHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char CharNum
 }

==0x67==
 struct PACKET_CH_MAKE_CHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char name[24]
  /* this+0x1a */ unsigned char Str
  /* this+0x1b */ unsigned char Agi
  /* this+0x1c */ unsigned char Vit
  /* this+0x1d */ unsigned char Int
  /* this+0x1e */ unsigned char Dex
  /* this+0x1f */ unsigned char Luk
  /* this+0x20 */ unsigned char CharNum
  /* this+0x21 */ short headPal
  /* this+0x23 */ short head
 }

==0x68==
 struct PACKET_CH_DELETE_CHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ char key[40]
 }

==0x69==
 struct PACKET_AC_ACCEPT_LOGIN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int AuthCode
  /* this+0x8 */ unsigned long AID
  /* this+0xc */ unsigned long userLevel
  /* this+0x10 */ unsigned long lastLoginIP
  /* this+0x14 */ char lastLoginTime[26]
  /* this+0x2e */ unsigned char Sex
  /* this+0x2f */ struct SERVER_ADDR ServerList[...] { // Size 32
    /* this+0x0 */ unsigned long ip
    /* this+0x4 */ short port
    /* this+0x6 */ unsigned char name[20]
    /* this+0x1a */ unsigned short usercount
    /* this+0x1c */ unsigned short state
    /* this+0x1e */ unsigned short property
  }
 }

==0x6a==
 struct PACKET_AC_REFUSE_LOGIN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
  /* this+0x3 */ char blockDate[20]
 }

==0x6b==
 struct PACKET_HC_ACCEPT_ENTER_NEO_UNION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char TotalSlotNum
  /* this+0x5 */ unsigned char PremiumStartSlot
  /* this+0x6 */ unsigned char PremiumEndSlot
  /* this+0x7 */ char dummy1_beginbilling
  /* this+0x8 */ unsigned long code
  /* this+0xc */ unsigned long time1
  /* this+0x10 */ unsigned long time2
  /* this+0x14 */ char dummy2_endbilling[7]
  /* this+0x1b */ struct CHARACTER_INFO_NEO_UNION charInfo[...] { // Size 144
    /* this+0x0 */ unsigned long GID
    /* this+0x4 */ int exp
    /* this+0x8 */ int money
    /* this+0xc */ int jobexp
    /* this+0x10 */ int joblevel
    /* this+0x14 */ int bodystate
    /* this+0x18 */ int healthstate
    /* this+0x1c */ int effectstate
    /* this+0x20 */ int virtue
    /* this+0x24 */ int honor
    /* this+0x28 */ short jobpoint
    /* this+0x2a */ int hp
    /* this+0x2e */ int maxhp
    /* this+0x32 */ short sp
    /* this+0x34 */ short maxsp
    /* this+0x36 */ short speed
    /* this+0x38 */ short job
    /* this+0x3a */ short head
    /* this+0x3c */ short weapon
    /* this+0x3e */ short level
    /* this+0x40 */ short sppoint
    /* this+0x42 */ short accessory
    /* this+0x44 */ short shield
    /* this+0x46 */ short accessory2
    /* this+0x48 */ short accessory3
    /* this+0x4a */ short headpalette
    /* this+0x4c */ short bodypalette
    /* this+0x4e */ unsigned char name[24]
    /* this+0x66 */ unsigned char Str
    /* this+0x67 */ unsigned char Agi
    /* this+0x68 */ unsigned char Vit
    /* this+0x69 */ unsigned char Int
    /* this+0x6a */ unsigned char Dex
    /* this+0x6b */ unsigned char Luk
    /* this+0x6c */ unsigned char CharNum
    /* this+0x6d */ unsigned char haircolor
    /* this+0x6e */ short bIsChangedCharName
    /* this+0x70 */ unsigned char lastMap[16]
    /* this+0x80 */ int DeleteDate
    /* this+0x84 */ int Robe
    /* this+0x88 */ int SlotAddon
    /* this+0x8c */ int RenameAddon
  }
 }

==0x6c==
 struct PACKET_HC_REFUSE_ENTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
 }

==0x6d==
 struct PACKET_HC_ACCEPT_MAKECHAR_NEO_UNION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct CHARACTER_INFO_NEO_UNION charinfo {
    /* this+0x0 */ unsigned long GID
    /* this+0x4 */ int exp
    /* this+0x8 */ int money
    /* this+0xc */ int jobexp
    /* this+0x10 */ int joblevel
    /* this+0x14 */ int bodystate
    /* this+0x18 */ int healthstate
    /* this+0x1c */ int effectstate
    /* this+0x20 */ int virtue
    /* this+0x24 */ int honor
    /* this+0x28 */ short jobpoint
    /* this+0x2a */ int hp
    /* this+0x2e */ int maxhp
    /* this+0x32 */ short sp
    /* this+0x34 */ short maxsp
    /* this+0x36 */ short speed
    /* this+0x38 */ short job
    /* this+0x3a */ short head
    /* this+0x3c */ short weapon
    /* this+0x3e */ short level
    /* this+0x40 */ short sppoint
    /* this+0x42 */ short accessory
    /* this+0x44 */ short shield
    /* this+0x46 */ short accessory2
    /* this+0x48 */ short accessory3
    /* this+0x4a */ short headpalette
    /* this+0x4c */ short bodypalette
    /* this+0x4e */ unsigned char name[24]
    /* this+0x66 */ unsigned char Str
    /* this+0x67 */ unsigned char Agi
    /* this+0x68 */ unsigned char Vit
    /* this+0x69 */ unsigned char Int
    /* this+0x6a */ unsigned char Dex
    /* this+0x6b */ unsigned char Luk
    /* this+0x6c */ unsigned char CharNum
    /* this+0x6d */ unsigned char haircolor
    /* this+0x6e */ short bIsChangedCharName
  }
 }

==0x6e==
 struct PACKET_HC_REFUSE_MAKECHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
 }

==0x6f==
 struct PACKET_HC_ACCEPT_DELETECHAR {
  /* this+0x0 */ short PacketType
 }

==0x70==
 struct PACKET_HC_REFUSE_DELETECHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
 }

==0x71==
 struct PACKET_HC_NOTIFY_ZONESVR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char mapName[16]
  /* this+0x16 */ struct ZSERVER_ADDR addr {
    /* this+0x0 */ unsigned long ip
    /* this+0x4 */ short port
  }
 }

==0x72==
 struct PACKET_CZ_ENTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ int AuthCode
  /* this+0xe */ unsigned long clientTime
  /* this+0x12 */ unsigned char Sex
 }

==0x73==
 struct PACKET_ZC_ACCEPT_ENTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long startTime
  /* this+0x6 */ unsigned char PosDir[3]
  /* this+0x9 */ unsigned char xSize
  /* this+0xa */ unsigned char ySize
 }

==0x74==
 struct PACKET_ZC_REFUSE_ENTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
 }

==0x75==
 struct PACKET_ZC_NOTIFY_INITCHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long GID
  /* this+0x8 */ short Style
  /* this+0xa */ unsigned char Item
 }

==0x76==
 struct PACKET_ZC_NOTIFY_UPDATECHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short Style
  /* this+0x8 */ unsigned char Item
 }

==0x77==
 struct PACKET_ZC_NOTIFY_UPDATEPLAYER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Style
  /* this+0x4 */ unsigned char Item
 }

==0x78==
 struct PACKET_ZC_NOTIFY_STANDENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char objecttype
  /* this+0x3 */ unsigned long GID
  /* this+0x7 */ short speed
  /* this+0x9 */ short bodyState
  /* this+0xb */ short healthState
  /* this+0xd */ short effectState
  /* this+0xf */ short job
  /* this+0x11 */ short head
  /* this+0x13 */ short weapon
  /* this+0x15 */ short accessory
  /* this+0x17 */ short shield
  /* this+0x19 */ short accessory2
  /* this+0x1b */ short accessory3
  /* this+0x1d */ short headpalette
  /* this+0x1f */ short bodypalette
  /* this+0x21 */ short headDir
  /* this+0x23 */ unsigned long GUID
  /* this+0x27 */ short GEmblemVer
  /* this+0x29 */ short honor
  /* this+0x2b */ short virtue
  /* this+0x2d */ bool isPKModeON
  /* this+0x2e */ unsigned char sex
  /* this+0x2f */ unsigned char PosDir[3]
  /* this+0x32 */ unsigned char xSize
  /* this+0x33 */ unsigned char ySize
  /* this+0x34 */ unsigned char state
  /* this+0x35 */ short clevel
 }

==0x79==
 struct PACKET_ZC_NOTIFY_NEWENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ short effectState
  /* this+0xe */ short job
  /* this+0x10 */ short head
  /* this+0x12 */ short weapon
  /* this+0x14 */ short accessory
  /* this+0x16 */ short shield
  /* this+0x18 */ short accessory2
  /* this+0x1a */ short accessory3
  /* this+0x1c */ short headpalette
  /* this+0x1e */ short bodypalette
  /* this+0x20 */ short headDir
  /* this+0x22 */ unsigned long GUID
  /* this+0x26 */ short GEmblemVer
  /* this+0x28 */ short honor
  /* this+0x2a */ short virtue
  /* this+0x2c */ bool isPKModeON
  /* this+0x2d */ unsigned char sex
  /* this+0x2e */ unsigned char PosDir[3]
  /* this+0x31 */ unsigned char xSize
  /* this+0x32 */ unsigned char ySize
  /* this+0x33 */ short clevel
 }

==0x7a==
 struct PACKET_ZC_NOTIFY_ACTENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ short effectState
  /* this+0xe */ short job
  /* this+0x10 */ short head
  /* this+0x12 */ short weapon
  /* this+0x14 */ short accessory
  /* this+0x16 */ short shield
  /* this+0x18 */ short accessory2
  /* this+0x1a */ short accessory3
  /* this+0x1c */ short headpalette
  /* this+0x1e */ short bodypalette
  /* this+0x20 */ short headDir
  /* this+0x22 */ unsigned long GUID
  /* this+0x26 */ short GEmblemVer
  /* this+0x28 */ short honor
  /* this+0x2a */ short virtue
  /* this+0x2c */ bool isPKModeON
  /* this+0x2d */ unsigned char sex
  /* this+0x2e */ unsigned char PosDir[3]
  /* this+0x31 */ unsigned char xSize
  /* this+0x32 */ unsigned char ySize
  /* this+0x33 */ unsigned char action
  /* this+0x34 */ unsigned long actStartTime
  /* this+0x38 */ short clevel
 }

==0x7b==
 struct PACKET_ZC_NOTIFY_MOVEENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ short effectState
  /* this+0xe */ short job
  /* this+0x10 */ short head
  /* this+0x12 */ short weapon
  /* this+0x14 */ short accessory
  /* this+0x16 */ unsigned long moveStartTime
  /* this+0x1a */ short shield
  /* this+0x1c */ short accessory2
  /* this+0x1e */ short accessory3
  /* this+0x20 */ short headpalette
  /* this+0x22 */ short bodypalette
  /* this+0x24 */ short headDir
  /* this+0x26 */ unsigned long GUID
  /* this+0x2a */ short GEmblemVer
  /* this+0x2c */ short honor
  /* this+0x2e */ short virtue
  /* this+0x30 */ bool isPKModeON
  /* this+0x31 */ unsigned char sex
  /* this+0x32 */ unsigned char MoveData[6]
  /* this+0x38 */ unsigned char xSize
  /* this+0x39 */ unsigned char ySize
  /* this+0x3a */ short clevel
 }

==0x7c==
 struct PACKET_ZC_NOTIFY_STANDENTRY_NPC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char objecttype
  /* this+0x3 */ unsigned long GID
  /* this+0x7 */ short speed
  /* this+0x9 */ short bodyState
  /* this+0xb */ short healthState
  /* this+0xd */ short effectState
  /* this+0xf */ short head
  /* this+0x11 */ short weapon
  /* this+0x13 */ short accessory
  /* this+0x15 */ short job
  /* this+0x17 */ short shield
  /* this+0x19 */ short accessory2
  /* this+0x1b */ short accessory3
  /* this+0x1d */ short headpalette
  /* this+0x1f */ short bodypalette
  /* this+0x21 */ short headDir
  /* this+0x23 */ bool isPKModeON
  /* this+0x24 */ unsigned char sex
  /* this+0x25 */ unsigned char PosDir[3]
  /* this+0x28 */ unsigned char xSize
  /* this+0x29 */ unsigned char ySize
 }

==0x7d==
 struct PACKET_CZ_NOTIFY_ACTORINIT {
  /* this+0x0 */ short PacketType
 }

==0x7e==
 struct PACKET_CZ_REQUEST_TIME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long clientTime
 }

==0x7f==
 struct PACKET_ZC_NOTIFY_TIME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long time
 }

==0x80==
 struct PACKET_ZC_NOTIFY_VANISH {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char type
 }

==0x81==
 struct PACKET_SC_NOTIFY_BAN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
 }

==0x82==
 struct PACKET_CZ_REQUEST_QUIT {
  /* this+0x0 */ short PacketType
 }

==0x83==
 struct PACKET_ZC_ACCEPT_QUIT {
  /* this+0x0 */ short PacketType
 }

==0x84==
 struct PACKET_ZC_REFUSE_QUIT {
  /* this+0x0 */ short PacketType
 }

==0x85==
 struct PACKET_CZ_REQUEST_MOVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char dest[3]
 }

==0x86==
 struct PACKET_ZC_NOTIFY_MOVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char MoveData[6]
  /* this+0xc */ unsigned long moveStartTime
 }

==0x87==
 struct PACKET_ZC_NOTIFY_PLAYERMOVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long moveStartTime
  /* this+0x6 */ unsigned char MoveData[6]
 }

==0x88==
 struct PACKET_ZC_STOPMOVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
 }

==0x89==
 struct PACKET_CZ_REQUEST_ACT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long targetGID
  /* this+0x6 */ unsigned char action
 }

==0x8a==
 struct PACKET_ZC_NOTIFY_ACT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned long targetGID
  /* this+0xa */ unsigned long startTime
  /* this+0xe */ int attackMT
  /* this+0x12 */ int attackedMT
  /* this+0x16 */ short damage
  /* this+0x18 */ short count
  /* this+0x1a */ unsigned char action
  /* this+0x1b */ short leftDamage
 }

==0x8b==
 struct PACKET_ZC_NOTIFY_ACT_POSITION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned long targetGID
  /* this+0xa */ unsigned long startTime
  /* this+0xe */ short xPos
  /* this+0x10 */ short yPos
  /* this+0x12 */ short damage
  /* this+0x14 */ short count
  /* this+0x16 */ unsigned char action
 }

==0x8c==
 struct PACKET_CZ_REQUEST_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x8d==
 struct PACKET_ZC_NOTIFY_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long GID
  /* this+0x8 */ char msg[...]
 }

==0x8e==
 struct PACKET_ZC_NOTIFY_PLAYERCHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x8f==
 struct PACKET_SERVER_ENTRY_ACK {
  /* this+0x0 */ short Header
  /* this+0x2 */ int AID
 }

==0x90==
 struct PACKET_CZ_CONTACTNPC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
  /* this+0x6 */ unsigned char type
 }

==0x91==
 struct PACKET_ZC_NPCACK_MAPMOVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char mapName[16]
  /* this+0x12 */ short xPos
  /* this+0x14 */ short yPos
 }

==0x92==
 struct PACKET_ZC_NPCACK_SERVERMOVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char mapName[16]
  /* this+0x12 */ short xPos
  /* this+0x14 */ short yPos
  /* this+0x16 */ struct ZSERVER_ADDR addr {
    /* this+0x0 */ unsigned long ip
    /* this+0x4 */ short port
  }
 }

==0x93==
 struct PACKET_ZC_NPCACK_ENABLE {
  /* this+0x0 */ short PacketType
 }

==0x94==
 struct PACKET_CZ_REQNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x95==
 struct PACKET_ZC_ACK_REQNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ char CName[24]
 }

==0x96==
 struct PACKET_CZ_WHISPER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char receiver[24]
  /* this+0x2c */ char msg[...]
 }

==0x97==
 struct PACKET_ZC_WHISPER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char sender[24]
  /* this+0x2c */ char msg[...]
 }

==0x98==
 struct PACKET_ZC_ACK_WHISPER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0x99==
 struct PACKET_CZ_BROADCAST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x9a==
 struct PACKET_ZC_BROADCAST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x9b==
 struct PACKET_CZ_CHANGE_DIRECTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short headDir
  /* this+0x4 */ unsigned char dir
 }

==0x9c==
 struct PACKET_ZC_CHANGE_DIRECTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short headDir
  /* this+0x8 */ unsigned char dir
 }

==0x9d==
 struct PACKET_ZC_ITEM_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ITAID
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ short xPos
  /* this+0xb */ short yPos
  /* this+0xd */ short count
  /* this+0xf */ unsigned char subX
  /* this+0x10 */ unsigned char subY
 }

==0x9e==
 struct PACKET_ZC_ITEM_FALL_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ITAID
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ short xPos
  /* this+0xb */ short yPos
  /* this+0xd */ unsigned char subX
  /* this+0xe */ unsigned char subY
  /* this+0xf */ short count
 }

==0x9f==
 struct PACKET_CZ_ITEM_PICKUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ITAID
 }

==0xa0==
 struct PACKET_ZC_ITEM_PICKUP_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Index
  /* this+0x4 */ unsigned short count
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ bool IsDamaged
  /* this+0xa */ unsigned char refiningLevel
  /* this+0xb */ struct EQUIPSLOTINFOEQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
  /* this+0x13 */ unsigned short location
  /* this+0x15 */ unsigned char type
  /* this+0x16 */ unsigned char result
 }

==0xa1==
 struct PACKET_ZC_ITEM_DISAPPEAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ITAID
 }

==0xa2==
 struct PACKET_CZ_ITEM_THROW {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Index
  /* this+0x4 */ short count
 }

==0xa3==
 struct PACKET_ZC_NORMAL_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO itemInfo[...] { // Size 10
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
  }
 }

==0xa4==
 struct PACKET_ZC_EQUIPMENT_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO itemInfo[...] { // Size 20
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0xa5==
 struct PACKET_ZC_STORE_NORMAL_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO itemInfo[...] { // Size 10
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
  }
 }

==0xa6==
 struct PACKET_ZC_STORE_EQUIPMENT_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO itemInfo[...] { // Size 20
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0xa7==
 struct PACKET_CZ_USE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ unsigned long AID
 }

==0xa8==
 struct PACKET_ZC_USE_ITEM_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ short count
  /* this+0x6 */ bool result
 }

==0xa9==
 struct PACKET_CZ_REQ_WEAR_EQUIP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ unsigned short wearLocation
 }

==0xaa==
 struct PACKET_ZC_REQ_WEAR_EQUIP_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ unsigned short wearLocation
  /* this+0x6 */ unsigned char result
 }

==0xab==
 struct PACKET_CZ_REQ_TAKEOFF_EQUIP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
 }

==0xac==
 struct PACKET_ZC_REQ_TAKEOFF_EQUIP_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ unsigned short wearLocation
  /* this+0x6 */ bool result
 }

==0xaf==
 struct PACKET_ZC_ITEM_THROW_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Index
  /* this+0x4 */ short count
 }

==0xb0==
 struct PACKET_ZC_PAR_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short varID
  /* this+0x4 */ int count
 }

==0xb1==
 struct PACKET_ZC_LONGPAR_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short varID
  /* this+0x4 */ int amount
 }

==0xb2==
 struct PACKET_CZ_RESTART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
 }

==0xb3==
 struct PACKET_ZC_RESTART_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
 }

==0xb4==
 struct PACKET_ZC_SAY_DIALOG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long NAID
  /* this+0x8 */ char msg[...]
 }

==0xb5==
 struct PACKET_ZC_WAIT_DIALOG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0xb6==
 struct PACKET_ZC_CLOSE_DIALOG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0xb7==
 struct PACKET_ZC_MENU_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long NAID
  /* this+0x8 */ char msg[...]
 }

==0xb8==
 struct PACKET_CZ_CHOOSE_MENU {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
  /* this+0x6 */ unsigned char num
 }

==0xb9==
 struct PACKET_CZ_REQ_NEXT_SCRIPT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0xba==
 struct PACKET_CZ_REQ_STATUS {
  /* this+0x0 */ short PacketType
 }

==0xbb==
 struct PACKET_CZ_STATUS_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short statusID
  /* this+0x4 */ unsigned char changeAmount
 }

==0xbc==
 struct PACKET_ZC_STATUS_CHANGE_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short statusID
  /* this+0x4 */ bool result
  /* this+0x5 */ unsigned char value
 }

==0xbd==
 struct PACKET_ZC_STATUS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short point
  /* this+0x4 */ unsigned char str
  /* this+0x5 */ unsigned char standardStr
  /* this+0x6 */ unsigned char agi
  /* this+0x7 */ unsigned char standardAgi
  /* this+0x8 */ unsigned char vit
  /* this+0x9 */ unsigned char standardVit
  /* this+0xa */ unsigned char Int
  /* this+0xb */ unsigned char standardInt
  /* this+0xc */ unsigned char dex
  /* this+0xd */ unsigned char standardDex
  /* this+0xe */ unsigned char luk
  /* this+0xf */ unsigned char standardLuk
  /* this+0x10 */ short attPower
  /* this+0x12 */ short refiningPower
  /* this+0x14 */ short max_mattPower
  /* this+0x16 */ short min_mattPower
  /* this+0x18 */ short itemdefPower
  /* this+0x1a */ short plusdefPower
  /* this+0x1c */ short mdefPower
  /* this+0x1e */ short plusmdefPower
  /* this+0x20 */ short hitSuccessValue
  /* this+0x22 */ short avoidSuccessValue
  /* this+0x24 */ short plusAvoidSuccessValue
  /* this+0x26 */ short criticalSuccessValue
  /* this+0x28 */ short ASPD
  /* this+0x2a */ short plusASPD
 }

==0xbe==
 struct PACKET_ZC_STATUS_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short statusID
  /* this+0x4 */ unsigned char value
 }

==0xbf==
 struct PACKET_CZ_REQ_EMOTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
 }

==0xc0==
 struct PACKET_ZC_EMOTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char type
 }

==0xc1==
 struct PACKET_CZ_REQ_USER_COUNT {
  /* this+0x0 */ short PacketType
 }

==0xc2==
 struct PACKET_ZC_USER_COUNT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int count
 }

==0xc3==
 struct PACKET_ZC_SPRITE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ unsigned char value
 }

==0xc4==
 struct PACKET_ZC_SELECT_DEALTYPE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0xc5==
 struct PACKET_CZ_ACK_SELECT_DEALTYPE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
  /* this+0x6 */ unsigned char type
 }

==0xc6==
 struct PACKET_ZC_PC_PURCHASE_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct PURCHASE_ITEM itemList[...] { // Size 11
    /* this+0x0 */ int price
    /* this+0x4 */ int discountprice
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
  }
 }

==0xc7==
 struct PACKET_ZC_PC_SELL_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct SELL_ITEM itemList[...] { // Size 10
    /* this+0x0 */ short index
    /* this+0x2 */ int price
    /* this+0x6 */ int overchargeprice
  }
 }

==0xc8==
 struct PACKET_CZ_PC_PURCHASE_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct CZ_PURCHASE_ITEM itemList[...] { // Size 4
    /* this+0x0 */ short count
    /* this+0x2 */ unsigned short ITID
  }
 }

==0xc9==
 struct PACKET_CZ_PC_SELL_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct CZ_SELL_ITEM itemList[...] { // Size 4
    /* this+0x0 */ short index
    /* this+0x2 */ short count
  }
 }

==0xca==
 struct PACKET_ZC_PC_PURCHASE_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xcb==
 struct PACKET_ZC_PC_SELL_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xcc==
 struct PACKET_CZ_DISCONNECT_CHARACTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0xcd==
 struct PACKET_ZC_ACK_DISCONNECT_CHARACTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xce==
 struct PACKET_CZ_DISCONNECT_ALL_CHARACTER {
  /* this+0x0 */ short PacketType
 }

==0xcf==
 struct PACKET_CZ_SETTING_WHISPER_PC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
  /* this+0x1a */ unsigned char type
 }

==0xd0==
 struct PACKET_CZ_SETTING_WHISPER_STATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
 }

==0xd1==
 struct PACKET_ZC_SETTING_WHISPER_PC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
  /* this+0x3 */ unsigned char result
 }

==0xd2==
 struct PACKET_ZC_SETTING_WHISPER_STATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
  /* this+0x3 */ unsigned char result
 }

==0xd3==
 struct PACKET_CZ_REQ_WHISPER_LIST {
  /* this+0x0 */ short PacketType
 }

==0xd4==
 struct PACKET_ZC_WHISPER_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct WHISPER_ITEM wisperList[...] { // Size 24
    /* this+0x0 */ char name[24]
  }
 }

==0xd5==
 struct PACKET_CZ_CREATE_CHATROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short size
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ char passwd[8]
  /* this+0xf */ char title[...]
 }

==0xd6==
 struct PACKET_ZC_ACK_CREATE_CHATROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xd7==
 struct PACKET_ZC_ROOM_NEWENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long roomID
  /* this+0xc */ short maxcount
  /* this+0xe */ short curcount
  /* this+0x10 */ unsigned char type
  /* this+0x11 */ char title[...]
 }

==0xd8==
 struct PACKET_ZC_DESTROY_ROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long roomID
 }

==0xd9==
 struct PACKET_CZ_REQ_ENTER_ROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long roomID
  /* this+0x6 */ char passwd[8]
 }

==0xda==
 struct PACKET_ZC_REFUSE_ENTER_ROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xdb==
 struct PACKET_ZC_ENTER_ROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long roomID
  /* this+0x8 */ struct ROOM_MEMBER memberList[...] { // Size 28
    /* this+0x0 */ unsigned long role
    /* this+0x4 */ char name[24]
  }
 }

==0xdc==
 struct PACKET_ZC_MEMBER_NEWENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short curcount
  /* this+0x4 */ char name[24]
 }

==0xdd==
 struct PACKET_ZC_MEMBER_EXIT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short curcount
  /* this+0x4 */ char name[24]
  /* this+0x1c */ unsigned char type
 }

==0xde==
 struct PACKET_CZ_CHANGE_CHATROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short size
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ char passwd[8]
  /* this+0xf */ char title[...]
 }

==0xdf==
 struct PACKET_ZC_CHANGE_CHATROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long roomID
  /* this+0xc */ short maxcount
  /* this+0xe */ short curcount
  /* this+0x10 */ unsigned char type
  /* this+0x11 */ char title[...]
 }

==0xe0==
 struct PACKET_CZ_REQ_ROLE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long role
  /* this+0x6 */ char name[24]
 }

==0xe1==
 struct PACKET_ZC_ROLE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long role
  /* this+0x6 */ char name[24]
 }

==0xe2==
 struct PACKET_CZ_REQ_EXPEL_MEMBER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
 }

==0xe3==
 struct PACKET_CZ_EXIT_ROOM {
  /* this+0x0 */ short PacketType
 }

==0xe4==
 struct PACKET_CZ_REQ_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0xe5==
 struct PACKET_ZC_REQ_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
 }

==0xe6==
 struct PACKET_CZ_ACK_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xe7==
 struct PACKET_ZC_ACK_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xe8==
 struct PACKET_CZ_ADD_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0xe9==
 struct PACKET_ZC_ADD_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int count
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ bool IsDamaged
  /* this+0xa */ unsigned char refiningLevel
  /* this+0xb */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
 }

==0xea==
 struct PACKET_ZC_ACK_ADD_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Index
  /* this+0x4 */ unsigned char result
 }

==0xeb==
 struct PACKET_CZ_CONCLUDE_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
 }

==0xec==
 struct PACKET_ZC_CONCLUDE_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char who
 }

==0xed==
 struct PACKET_CZ_CANCEL_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
 }

==0xee==
 struct PACKET_ZC_CANCEL_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
 }

==0xef==
 struct PACKET_CZ_EXEC_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
 }

==0xf0==
 struct PACKET_ZC_EXEC_EXCHANGE_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xf1==
 struct PACKET_ZC_EXCHANGEITEM_UNDO {
  /* this+0x0 */ short PacketType
 }

==0xf2==
 struct PACKET_ZC_NOTIFY_STOREITEM_COUNTINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short curCount
  /* this+0x4 */ short maxCount
 }

==0xf3==
 struct PACKET_CZ_MOVE_ITEM_FROM_BODY_TO_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0xf4==
 struct PACKET_ZC_ADD_ITEM_TO_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
  /* this+0x8 */ unsigned short ITID
  /* this+0xa */ bool IsIdentified
  /* this+0xb */ bool IsDamaged
  /* this+0xc */ unsigned char refiningLevel
  /* this+0xd */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
 }

==0xf5==
 struct PACKET_CZ_MOVE_ITEM_FROM_STORE_TO_BODY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0xf6==
 struct PACKET_ZC_DELETE_ITEM_FROM_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0xf7==
 struct PACKET_CZ_CLOSE_STORE {
  /* this+0x0 */ short PacketType
 }

==0xf8==
 struct PACKET_ZC_CLOSE_STORE {
  /* this+0x0 */ short PacketType
 }

==0xf9==
 struct PACKET_CZ_MAKE_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char groupName[24]
 }

==0xfa==
 struct PACKET_ZC_ACK_MAKE_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0xfb==
 struct PACKET_ZC_GROUP_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char groupName[24]
  /* this+0x1c */ struct GROUPMEMBER_INFO groupInfo[...] { // Size 46
    /* this+0x0 */ unsigned long AID
    /* this+0x4 */ char characterName[24]
    /* this+0x1c */ char mapName[16]
    /* this+0x2c */ unsigned char role
    /* this+0x2d */ unsigned char state
  }
 }

==0xfc==
 struct PACKET_CZ_REQ_JOIN_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0xfd==
 struct PACKET_ZC_ACK_REQ_JOIN_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char characterName[24]
  /* this+0x1a */ unsigned char answer
 }

==0xfe==
 struct PACKET_ZC_REQ_JOIN_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GRID
  /* this+0x6 */ char groupName[24]
 }

==0xff==
 struct PACKET_CZ_JOIN_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GRID
  /* this+0x6 */ int answer
 }

==0x100==
 struct PACKET_CZ_REQ_LEAVE_GROUP {
  /* this+0x0 */ short PacketType
 }

==0x101==
 struct PACKET_ZC_GROUPINFO_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long expOption
 }

==0x102==
 struct PACKET_CZ_CHANGE_GROUPEXPOPTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long expOption
 }

==0x103==
 struct PACKET_CZ_REQ_EXPEL_GROUP_MEMBER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ char characterName[24]
 }

==0x104==
 struct PACKET_ZC_ADD_MEMBER_TO_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long Role
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned char state
  /* this+0xf */ char groupName[24]
  /* this+0x27 */ char characterName[24]
  /* this+0x3f */ char mapName[16]
 }

==0x105==
 struct PACKET_ZC_DELETE_MEMBER_FROM_GROUP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ char characterName[24]
  /* this+0x1e */ unsigned char result
 }

==0x106==
 struct PACKET_ZC_NOTIFY_HP_TO_GROUPM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short hp
  /* this+0x8 */ short maxhp
 }

==0x107==
 struct PACKET_ZC_NOTIFY_POSITION_TO_GROUPM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
 }

==0x108==
 struct PACKET_CZ_REQUEST_CHAT_PARTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x109==
 struct PACKET_ZC_NOTIFY_CHAT_PARTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ char msg[...]
 }

==0x10a==
 struct PACKET_ZC_MVP_GETTING_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ITID
 }

==0x10b==
 struct PACKET_ZC_MVP_GETTING_SPECIAL_EXP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long exp
 }

==0x10c==
 struct PACKET_ZC_MVP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x10d==
 struct PACKET_ZC_THROW_MVPITEM {
  /* this+0x0 */ short PacketType
 }

==0x10e==
 struct PACKET_ZC_SKILLINFO_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ short level
  /* this+0x6 */ short spcost
  /* this+0x8 */ short attackRange
  /* this+0xa */ bool upgradable
 }

==0x10f==
 struct PACKET_ZC_SKILLINFO_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct SKILLINFO skillList[...] { // Size 37
    /* this+0x0 */ short SKID
    /* this+0x2 */ int type
    /* this+0x6 */ short level
    /* this+0x8 */ short spcost
    /* this+0xa */ short attackRange
    /* this+0xc */ unsigned char skillName[24]
    /* this+0x24 */ char upgradable
  }
 }

==0x110==
 struct PACKET_ZC_ACK_TOUSESKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ unsigned long NUM
  /* this+0x8 */ bool result
  /* this+0x9 */ unsigned char cause
 }

==0x111==
 struct PACKET_ZC_ADD_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct SKILLINFO data {
    /* this+0x0 */ unsigned short SKID
    /* this+0x2 */ int type
    /* this+0x6 */ short level
    /* this+0x8 */ short spcost
    /* this+0xa */ short attackRange
    /* this+0xc */ char skillName[24]
    /* this+0x24 */ bool upgradable
  }
 }

==0x112==
 struct PACKET_CZ_UPGRADE_SKILLLEVEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
 }

==0x113==
 struct PACKET_CZ_USE_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short selectedLevel
  /* this+0x4 */ unsigned short SKID
  /* this+0x6 */ unsigned long targetID
 }

==0x114==
 struct PACKET_ZC_NOTIFY_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long targetID
  /* this+0xc */ unsigned long startTime
  /* this+0x10 */ int attackMT
  /* this+0x14 */ int attackedMT
  /* this+0x18 */ short damage
  /* this+0x1a */ short level
  /* this+0x1c */ short count
  /* this+0x1e */ unsigned char action
 }

==0x115==
 struct PACKET_ZC_NOTIFY_SKILL_POSITION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long targetID
  /* this+0xc */ unsigned long startTime
  /* this+0x10 */ int attackMT
  /* this+0x14 */ int attackedMT
  /* this+0x18 */ short xPos
  /* this+0x1a */ short yPos
  /* this+0x1c */ short damage
  /* this+0x1e */ short level
  /* this+0x20 */ short count
  /* this+0x22 */ unsigned char action
 }

==0x116==
 struct PACKET_CZ_USE_SKILL_TOGROUND {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short selectedLevel
  /* this+0x4 */ unsigned short SKID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
 }

==0x117==
 struct PACKET_ZC_NOTIFY_GROUNDSKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ short level
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned long startTime
 }

==0x118==
 struct PACKET_CZ_CANCEL_LOCKON {
  /* this+0x0 */ short PacketType
 }

==0x119==
 struct PACKET_ZC_STATE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short bodyState
  /* this+0x8 */ short healthState
  /* this+0xa */ short effectState
  /* this+0xc */ bool isPKModeON
 }

==0x11a==
 struct PACKET_ZC_USE_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ short level
  /* this+0x6 */ unsigned long targetAID
  /* this+0xa */ unsigned long srcAID
  /* this+0xe */ bool result
 }

==0x11b==
 struct PACKET_CZ_SELECT_WARPPOINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ char mapName[16]
 }

==0x11c==
 struct PACKET_ZC_WARPLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ char mapName[4][16]
 }

==0x11d==
 struct PACKET_CZ_REMEMBER_WARPPOINT {
  /* this+0x0 */ short PacketType
 }

==0x11e==
 struct PACKET_ZC_ACK_REMEMBER_WARPPOINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char errorCode
 }

==0x11f==
 struct PACKET_ZC_SKILL_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long creatorAID
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned char job
  /* this+0xf */ bool isVisible
 }

==0x120==
 struct PACKET_ZC_SKILL_DISAPPEAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x121==
 struct PACKET_ZC_NOTIFY_CARTITEM_COUNTINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short curCount
  /* this+0x4 */ short maxCount
  /* this+0x6 */ int curWeight
  /* this+0xa */ int maxWeight
 }

==0x122==
 struct PACKET_ZC_CART_EQUIPMENT_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO itemInfo[...] { // Size 20
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x123==
 struct PACKET_ZC_CART_NORMAL_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO itemInfo[...] { // Size 10
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
  }
 }

==0x124==
 struct PACKET_ZC_ADD_ITEM_TO_CART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
  /* this+0x8 */ unsigned short ITID
  /* this+0xa */ bool IsIdentified
  /* this+0xb */ bool IsDamaged
  /* this+0xc */ unsigned char refiningLevel
  /* this+0xd */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
 }

==0x125==
 struct PACKET_ZC_DELETE_ITEM_FROM_CART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x126==
 struct PACKET_CZ_MOVE_ITEM_FROM_BODY_TO_CART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x127==
 struct PACKET_CZ_MOVE_ITEM_FROM_CART_TO_BODY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x128==
 struct PACKET_CZ_MOVE_ITEM_FROM_STORE_TO_CART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x129==
 struct PACKET_CZ_MOVE_ITEM_FROM_CART_TO_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x12a==
 struct PACKET_CZ_REQ_CARTOFF {
  /* this+0x0 */ short PacketType
 }

==0x12b==
 struct PACKET_ZC_CARTOFF {
  /* this+0x0 */ short PacketType
 }

==0x12c==
 struct PACKET_ZC_ACK_ADDITEM_TO_CART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0x12d==
 struct PACKET_ZC_OPENSTORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short itemcount
 }

==0x12e==
 struct PACKET_CZ_REQ_CLOSESTORE {
  /* this+0x0 */ short PacketType
 }

==0x12f==
 struct PACKET_CZ_REQ_OPENSTORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char storeName[80]
  /* this+0x54 */ struct STORE_ITEM storeList[...] { // Size 8
    /* this+0x0 */ short index
    /* this+0x2 */ short count
    /* this+0x4 */ int Price
  }
 }

==0x130==
 struct PACKET_CZ_REQ_BUY_FROMMC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x131==
 struct PACKET_ZC_STORE_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long makerAID
  /* this+0x6 */ char storeName[80]
 }

==0x132==
 struct PACKET_ZC_DISAPPEAR_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long makerAID
 }

==0x133==
 struct PACKET_ZC_PC_PURCHASE_ITEMLIST_FROMMC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ struct PURCHASE_ITEM_FROMMC itemList[...] { // Size 22
    /* this+0x0 */ int price
    /* this+0x4 */ short count
    /* this+0x6 */ short index
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
    /* this+0xb */ unsigned char IsIdentified
    /* this+0xc */ unsigned char IsDamaged
    /* this+0xd */ unsigned char refiningLevel
    /* this+0xe */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x134==
 struct PACKET_CZ_PC_PURCHASE_ITEMLIST_FROMMC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ struct CZ_PURCHASE_ITEM_FROMMC itemList[...] { // Size 4
    /* this+0x0 */ short count
    /* this+0x2 */ short index
  }
 }

==0x135==
 struct PACKET_ZC_PC_PURCHASE_RESULT_FROMMC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ short curcount
  /* this+0x6 */ unsigned char result
 }

==0x136==
 struct PACKET_ZC_PC_PURCHASE_MYITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ struct PURCHASE_MYITEM itemList[...] { // Size 22
    /* this+0x0 */ int price
    /* this+0x4 */ short index
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
    /* this+0xb */ unsigned char IsIdentified
    /* this+0xc */ unsigned char IsDamaged
    /* this+0xd */ unsigned char refiningLevel
    /* this+0xe */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x137==
 struct PACKET_ZC_DELETEITEM_FROM_MCSTORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ short count
 }

==0x138==
 struct PACKET_CZ_PKMODE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool isTurnOn
 }

==0x139==
 struct PACKET_ZC_ATTACK_FAILURE_FOR_DISTANCE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long targetAID
  /* this+0x6 */ short targetXPos
  /* this+0x8 */ short targetYPos
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ short currentAttRange
 }

==0x13a==
 struct PACKET_ZC_ATTACK_RANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short currentAttRange
 }

==0x13b==
 struct PACKET_ZC_ACTION_FAILURE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x13c==
 struct PACKET_ZC_EQUIP_ARROW {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
 }

==0x13d==
 struct PACKET_ZC_RECOVERY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short varID
  /* this+0x4 */ short amount
 }

==0x13e==
 struct PACKET_ZC_USESKILL_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long targetID
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned short SKID
  /* this+0x10 */ unsigned long property
  /* this+0x14 */ unsigned long delayTime
 }

==0x13f==
 struct PACKET_CZ_ITEM_CREATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char itemName[24]
 }

==0x140==
 struct PACKET_CZ_MOVETO_MAP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char mapName[16]
  /* this+0x12 */ short xPos
  /* this+0x14 */ short yPos
 }

==0x141==
 struct PACKET_ZC_COUPLESTATUS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long statusType
  /* this+0x6 */ int defaultStatus
  /* this+0xa */ int plusStatus
 }

==0x142==
 struct PACKET_ZC_OPEN_EDITDLG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0x143==
 struct PACKET_CZ_INPUT_EDITDLG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
  /* this+0x6 */ int value
 }

==0x144==
 struct PACKET_ZC_COMPASS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
  /* this+0x6 */ int type
  /* this+0xa */ int xPos
  /* this+0xe */ int yPos
  /* this+0x12 */ unsigned char id
  /* this+0x13 */ unsigned long color
 }

==0x145==
 struct PACKET_ZC_SHOW_IMAGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char imageName[16]
  /* this+0x12 */ unsigned char type
 }

==0x146==
 struct PACKET_CZ_CLOSE_DIALOG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0x147==
 struct PACKET_ZC_AUTORUN_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct SKILLINFO data {
    /* this+0x0 */ unsigned short SKID
    /* this+0x2 */ int type
    /* this+0x6 */ short level
    /* this+0x8 */ short spcost
    /* this+0xa */ short attackRange
    /* this+0xc */ char skillName[24]
    /* this+0x24 */ bool upgradable
  }
 }

==0x148==
 struct PACKET_ZC_RESURRECTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short type
 }

==0x149==
 struct PACKET_CZ_REQ_GIVE_MANNER_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long otherAID
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ short point
 }

==0x14a==
 struct PACKET_ZC_ACK_GIVE_MANNER_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long result
 }

==0x14b==
 struct PACKET_ZC_NOTIFY_MANNER_POINT_GIVEN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
  /* this+0x3 */ char otherCharName[24]
 }

==0x14c==
 struct PACKET_ZC_MYGUILD_BASIC_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct RELATED_GUILD relatedGuildList[...] { // Size 32
    /* this+0x0 */ int GDID
    /* this+0x4 */ int relation
    /* this+0x8 */ char GuildName[24]
  }
 }

==0x14d==
 struct PACKET_CZ_REQ_GUILD_MENUINTERFACE {
  /* this+0x0 */ short PacketType
 }

==0x14e==
 struct PACKET_ZC_ACK_GUILD_MENUINTERFACE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int guildMemuFlag
 }

==0x14f==
 struct PACKET_CZ_REQ_GUILD_MENU {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Type
 }

==0x150==
 struct PACKET_ZC_GUILD_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int GDID
  /* this+0x6 */ int level
  /* this+0xa */ int userNum
  /* this+0xe */ int maxUserNum
  /* this+0x12 */ int userAverageLevel
  /* this+0x16 */ int exp
  /* this+0x1a */ int maxExp
  /* this+0x1e */ int point
  /* this+0x22 */ int honor
  /* this+0x26 */ int virtue
  /* this+0x2a */ int emblemVersion
  /* this+0x2e */ char guildname[24]
  /* this+0x46 */ char masterName[24]
  /* this+0x5e */ char manageLand[16]
 }

==0x151==
 struct PACKET_CZ_REQ_GUILD_EMBLEM_IMG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int GDID
 }

==0x152==
 struct PACKET_ZC_GUILD_EMBLEM_IMG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int GDID
  /* this+0x8 */ int emblemVersion
  /* this+0xc */ unsigned char img[...]
 }

==0x153==
 struct PACKET_CZ_REGISTER_GUILD_EMBLEM_IMG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char img[...]
 }

==0x154==
 struct PACKET_ZC_MEMBERMGR_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct GUILD_MEMBERMGR_INFO memberInfo[...] { // Size 104
    /* this+0x0 */ unsigned long AID
    /* this+0x4 */ unsigned long GID
    /* this+0x8 */ short HeadType
    /* this+0xa */ short HeadPalette
    /* this+0xc */ short Sex
    /* this+0xe */ short Job
    /* this+0x10 */ short Level
    /* this+0x12 */ int MemberExp
    /* this+0x16 */ int CurrentState
    /* this+0x1a */ int GPositionID
    /* this+0x1e */ char Memo[50]
    /* this+0x50 */ char CharName[24]
  }
 }

==0x155==
 struct PACKET_CZ_REQ_CHANGE_MEMBERPOS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct MEMBER_POSITION_INFO memberInfo[...] { // Size 12
    /* this+0x0 */ int AID
    /* this+0x4 */ int GID
    /* this+0x8 */ int positionID
  }
 }

==0x156==
 struct PACKET_ZC_ACK_REQ_CHANGE_MEMBERS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct MEMBER_POSITION_INFO memberInfo[...] { // Size 12
    /* this+0x0 */ int AID
    /* this+0x4 */ int GID
    /* this+0x8 */ int positionID
  }
 }

==0x157==
 struct PACKET_CZ_REQ_OPEN_MEMBER_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int AID
 }

==0x158==
 struct PACKET_ZC_ACK_OPEN_MEMBER_INFO {
  /* this+0x0 */ short PacketType
 }

==0x159==
 struct PACKET_CZ_REQ_LEAVE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ int AID
  /* this+0xa */ int GID
  /* this+0xe */ char reasonDesc[40]
 }

==0x15a==
 struct PACKET_ZC_ACK_LEAVE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char charName[24]
  /* this+0x1a */ char reasonDesc[40]
 }

==0x15b==
 struct PACKET_CZ_REQ_BAN_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ int AID
  /* this+0xa */ int GID
  /* this+0xe */ char reasonDesc[40]
 }

==0x15c==
 struct PACKET_ZC_ACK_BAN_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char charName[24]
  /* this+0x1a */ char reasonDesc[40]
  /* this+0x42 */ char account[24]
 }

==0x15d==
 struct PACKET_CZ_REQ_DISORGANIZE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char key[40]
 }

==0x15e==
 struct PACKET_ZC_ACK_DISORGANIZE_GUILD_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int reason
 }

==0x15f==
 struct PACKET_ZC_ACK_DISORGANIZE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char reasonDesc[40]
 }

==0x160==
 struct PACKET_ZC_POSITION_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct GUILD_MEMBER_POSITION_INFO memberInfo[...] { // Size 16
    /* this+0x0 */ int positionID
    /* this+0x4 */ int right
    /* this+0x8 */ int ranking
    /* this+0xC */ int payRate
  }
 }

==0x161==
 struct PACKET_CZ_REG_CHANGE_GUILD_POSITIONINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct GUILD_REG_POSITION_INFO memberList[...] { // Size 40
    /* this+0x0 */ int positionID
    /* this+0x4 */ int right
    /* this+0x8 */ int ranking
    /* this+0xc */ int payRate
    /* this+0x10 */ char posName[24]
  }
 }

==0x162==
 struct PACKET_ZC_GUILD_SKILLINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short skillPoint
  /* this+0x6 */ struct SKILLINFO skillList[...] { // Size 37
    /* this+0x0 */ unsigned short SKID
    /* this+0x2 */ int type
    /* this+0x6 */ short level
    /* this+0x8 */ short spcost
    /* this+0xa */ short attackRange
    /* this+0xc */ char skillName[24]
    /* this+0x24 */ char upgradable
  }
 }

==0x163==
 struct PACKET_ZC_BAN_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct GUILD_BAN_INFO banList[...] { // Size 88
    /* this+0x0 */ char charname[24]
    /* this+0x18 */ char account[24]
    /* this+0x30 */ char reason[40]
  }
 }

==0x164==
 struct PACKET_ZC_OTHER_GUILD_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct OTHER_GUILD_INFO guildList[...] { // Size 36
    /* this+0x0 */ char guildname[24]
    /* this+0x18 */ int guildLevel
    /* this+0x1c */ int guildMemberSize
    /* this+0x20 */ int guildRanking
  }
 }

==0x165==
 struct PACKET_CZ_REQ_MAKE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ char GName[24]
 }

==0x166==
 struct PACKET_ZC_POSITION_ID_NAME_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct MEMBER_POSITION_ID_NAME_INFO memberList[...] { // Size 28
    /* this+0x0 */ int positionID
    /* this+0x4 */ char posName[24]
  }
 }

==0x167==
 struct PACKET_ZC_RESULT_MAKE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0x168==
 struct PACKET_CZ_REQ_JOIN_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long MyAID
  /* this+0xa */ unsigned long MyGID
 }

==0x169==
 struct PACKET_ZC_ACK_REQ_JOIN_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char answer
 }

==0x16a==
 struct PACKET_ZC_REQ_JOIN_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ char guildName[24]
 }

==0x16b==
 struct PACKET_CZ_JOIN_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ int answer
 }

==0x16c==
 struct PACKET_ZC_UPDATE_GDID {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ int emblemVersion
  /* this+0xa */ int right
  /* this+0xe */ bool isMaster
  /* this+0xf */ int InterSID
  /* this+0x13 */ char GName[24]
 }

==0x16d==
 struct PACKET_ZC_UPDATE_CHARSTAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ int status
 }

==0x16e==
 struct PACKET_CZ_GUILD_NOTICE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ char subject[60]
  /* this+0x42 */ char notice[120]
 }

==0x16f==
 struct PACKET_ZC_GUILD_NOTICE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char subject[60]
  /* this+0x3e */ char notice[120]
 }

==0x170==
 struct PACKET_CZ_REQ_ALLY_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long MyAID
  /* this+0xa */ unsigned long MyGID
 }

==0x171==
 struct PACKET_ZC_REQ_ALLY_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long otherAID
  /* this+0x6 */ char guildName[24]
 }

==0x172==
 struct PACKET_CZ_ALLY_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long otherAID
  /* this+0x6 */ int answer
 }

==0x173==
 struct PACKET_ZC_ACK_REQ_ALLY_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char answer
 }

==0x174==
 struct PACKET_ZC_ACK_CHANGE_GUILD_POSITIONINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct GUILD_REG_POSITION_INFO memberList[...] { // Size 30
    /* this+0x0 */ int positionID
    /* this+0x4 */ int right
    /* this+0x8 */ int ranking
    /* this+0xc */ int payRate
    /* this+0x10 */ char posName[24]
  }
 }

==0x175==
 struct PACKET_CZ_REQ_GUILD_MEMBER_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int GID
 }

==0x176==
 struct PACKET_ZC_ACK_GUILD_MEMBER_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct GUILD_MEMBER_INFO Info {
    /* this+0x0 */ int AID
    /* this+0x4 */ int GID
    /* this+0x8 */ short head
    /* this+0xa */ short headPalette
    /* this+0xc */ short sex
    /* this+0xe */ short job
    /* this+0x10 */ short level
    /* this+0x12 */ int contributionExp
    /* this+0x16 */ int currentState
    /* this+0x1a */ int positionID
    /* this+0x1e */ char intro[50]
    /* this+0x50 */ char charname[24]
  }
 }

==0x177==
 struct PACKET_ZC_ITEMIDENTIFY_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned short ITIDList[...]
 }

==0x178==
 struct PACKET_CZ_REQ_ITEMIDENTIFY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
 }

==0x179==
 struct PACKET_ZC_ACK_ITEMIDENTIFY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ unsigned char result
 }

==0x17a==
 struct PACKET_CZ_REQ_ITEMCOMPOSITION_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short cardIndex
 }

==0x17b==
 struct PACKET_ZC_ITEMCOMPOSITION_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned short ITIDList[...]
 }

==0x17c==
 struct PACKET_CZ_REQ_ITEMCOMPOSITION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short cardIndex
  /* this+0x4 */ short equipIndex
 }

==0x17d==
 struct PACKET_ZC_ACK_ITEMCOMPOSITION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short equipIndex
  /* this+0x4 */ short cardIndex
  /* this+0x6 */ unsigned char result
 }

==0x17e==
 struct PACKET_CZ_GUILD_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x17f==
 struct PACKET_ZC_GUILD_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x180==
 struct PACKET_CZ_REQ_HOSTILE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x181==
 struct PACKET_ZC_ACK_REQ_HOSTILE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0x182==
 struct PACKET_ZC_MEMBER_ADD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct GUILD_MEMBER_INFO Info {
    /* this+0x0 */ int AID
    /* this+0x4 */ int GID
    /* this+0x8 */ short head
    /* this+0xa */ short headPalette
    /* this+0xc */ short sex
    /* this+0xe */ short job
    /* this+0x10 */ short level
    /* this+0x12 */ int contributionExp
    /* this+0x16 */ int currentState
    /* this+0x1a */ int positionID
    /* this+0x1e */ char intro[50]
    /* this+0x50 */ char charname[24]
  }
 }

==0x183==
 struct PACKET_CZ_REQ_DELETE_RELATED_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long OpponentGDID
  /* this+0x6 */ int Relation
 }

==0x184==
 struct PACKET_ZC_DELETE_RELATED_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long OpponentGDID
  /* this+0x6 */ int Relation
 }

==0x185==
 struct PACKET_ZC_ADD_RELATED_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct RELATED_GUILD_INFO Info {
    /* this+0x0 */ int relation
    /* this+0x4 */ int GDID
    /* this+0x8 */ char guildname[24]
  }
 }

==0x186==
 struct PACKET_COLLECTORDEAD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ServerID
 }

==0x187==
 struct PACKET_PING {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x188==
 struct PACKET_ZC_ACK_ITEMREFINING {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short result
  /* this+0x4 */ short itemIndex
  /* this+0x6 */ short refiningLevel
 }

==0x189==
 struct PACKET_ZC_NOTIFY_MAPINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short type
 }

==0x18a==
 struct PACKET_CZ_REQ_DISCONNECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short type
 }

==0x18b==
 struct PACKET_ZC_ACK_REQ_DISCONNECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short result
 }

==0x18c==
 struct PACKET_ZC_MONSTER_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short job
  /* this+0x4 */ short level
  /* this+0x6 */ short size
  /* this+0x8 */ int hp
  /* this+0xc */ short def
  /* this+0xe */ short raceType
  /* this+0x10 */ short mdefPower
  /* this+0x12 */ short property
  /* this+0x14 */  struct PACKET_ZC_MONSTER_INFO propertyTable {
    /* this+0x0 */ unsigned char water
    /* this+0x1 */ unsigned char earth
    /* this+0x2 */ unsigned char fire
    /* this+0x3 */ unsigned char wind
    /* this+0x4 */ unsigned char poison
    /* this+0x5 */ unsigned char saint
    /* this+0x6 */ unsigned char dark
    /* this+0x7 */ unsigned char mental
    /* this+0x8 */ unsigned char undead
  }
 }

==0x18d==
 struct PACKET_ZC_MAKABLEITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct MAKABLEITEM_INFO info {
    /* this+0x0 */ unsigned short ITID
    /* this+0x2 */ unsigned short material_ID[3]
  }
 }

==0x18e==
 struct PACKET_CZ_REQMAKINGITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct MAKABLEITEM_INFO info {
    /* this+0x0 */ unsigned short ITID
    /* this+0x2 */ unsigned short material_ID[3]
  }
 }

==0x18f==
 struct PACKET_ZC_ACK_REQMAKINGITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short result
  /* this+0x4 */ unsigned short ITID
 }

==0x190==
 struct PACKET_CZ_USE_SKILL_TOGROUND_WITHTALKBOX {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short selectedLevel
  /* this+0x4 */ unsigned short SKID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
  /* this+0xa */ char contents[80]
 }

==0x191==
 struct PACKET_ZC_TALKBOX_CHATCONTENTS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ char contents[80]
 }

==0x192==
 struct PACKET_ZC_UPDATE_MAPINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short xPos
  /* this+0x4 */ short yPos
  /* this+0x6 */ short type
  /* this+0x8 */ char mapName[16]
 }

==0x193==
 struct PACKET_CZ_REQNAME_BYGID {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
 }

==0x194==
 struct PACKET_ZC_ACK_REQNAME_BYGID {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ char CName[24]
 }

==0x195==
 struct PACKET_ZC_ACK_REQNAMEALL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ char CName[24]
  /* this+0x1e */ char PName[24]
  /* this+0x36 */ char GName[24]
  /* this+0x4e */ char RName[24]
 }

==0x196==
 struct PACKET_ZC_MSG_STATE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ bool state
 }

==0x197==
 struct PACKET_CZ_RESET {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short type
 }

==0x198==
 struct PACKET_CZ_CHANGE_MAPTYPE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short xPos
  /* this+0x4 */ short yPos
  /* this+0x6 */ short type
 }

==0x199==
 struct PACKET_ZC_NOTIFY_MAPPROPERTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short type
 }

==0x19a==
 struct PACKET_ZC_NOTIFY_RANKING {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int ranking
  /* this+0xa */ int total
 }

==0x19b==
 struct PACKET_ZC_NOTIFY_EFFECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int effectID
 }

==0x19d==
 struct PACKET_CZ_CHANGE_EFFECTSTATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int EffectState
 }

==0x19e==
 struct PACKET_ZC_START_CAPTURE {
  /* this+0x0 */ short PacketType
 }

==0x19f==
 struct PACKET_CZ_TRYCAPTURE_MONSTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long targetAID
 }

==0x1a0==
 struct PACKET_ZC_TRYCAPTURE_MONSTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
 }

==0x1a1==
 struct PACKET_CZ_COMMAND_PET {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char cSub
 }

==0x1a2==
 struct PACKET_ZC_PROPERTY_PET {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char szName[24]
  /* this+0x1a */ unsigned char bModified
  /* this+0x1b */ short nLevel
  /* this+0x1d */ short nFullness
  /* this+0x1f */ short nRelationship
  /* this+0x21 */ unsigned short ITID
  /* this+0x23 */ short job
 }

==0x1a3==
 struct PACKET_ZC_FEED_PET {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char cRet
  /* this+0x3 */ unsigned short ITID
 }

==0x1a4==
 struct PACKET_ZC_CHANGESTATE_PET {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char type
  /* this+0x3 */ int GID
  /* this+0x7 */ int data
 }

==0x1a5==
 struct PACKET_CZ_RENAME_PET {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char szName[24]
 }

==0x1a6==
 struct PACKET_ZC_PETEGG_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct PETEGGITEM_INFO eggList[...] { // Size 2
    /* this+0x0 */ short index
  }
 }

==0x1a7==
 struct PACKET_CZ_SELECT_PETEGG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
 }

==0x1a8==
 struct PACKET_CZ_PETEGG_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
 }

==0x1a9==
 struct PACKET_CZ_PET_ACT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int data
 }

==0x1aa==
 struct PACKET_ZC_PET_ACT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int GID
  /* this+0x6 */ int data
 }

==0x1ab==
 struct PACKET_ZC_PAR_CHANGE_USER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned short varID
  /* this+0x8 */ int count
 }

==0x1ac==
 struct PACKET_ZC_SKILL_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x1ad==
 struct PACKET_ZC_MAKINGARROW_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct ARROWITEM_INFO arrowList[...] { // Size 2
    /* this+0x0 */ short index
  }
 }

==0x1ae==
 struct PACKET_CZ_REQ_MAKINGARROW {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short id
 }

==0x1af==
 struct PACKET_CZ_REQ_CHANGECART {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short num
 }

==0x1b0==
 struct PACKET_ZC_NPCSPRITE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ unsigned long value
 }

==0x1b1==
 struct PACKET_ZC_SHOWDIGIT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char type
  /* this+0x3 */ int value
 }

==0x1b2==
 struct PACKET_CZ_REQ_OPENSTORE2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char storeName[80]
  /* this+0x54 */ bool result
  /* this+0x55 */ struct STORE_ITEM storeList[...] { // Size 8
    /* this+0x0 */ short index
    /* this+0x2 */ short count
    /* this+0x4 */ int Price
  }
 }

==0x1b3==
 struct PACKET_ZC_SHOW_IMAGE2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char imageName[64]
  /* this+0x42 */ unsigned char type
 }

==0x1b4==
 struct PACKET_ZC_CHANGE_GUILD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GDID
  /* this+0xa */ short emblemVersion
 }

==0x1b5==
 struct PACKET_SC_BILLING_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long dwAmountRemain
  /* this+0x6 */ unsigned long dwQuantityRemain
  /* this+0xa */ unsigned long dwReserved1
  /* this+0xe */ unsigned long dwReserved2
 }

==0x1b6==
 struct PACKET_ZC_GUILD_INFO2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int GDID
  /* this+0x6 */ int level
  /* this+0xa */ int userNum
  /* this+0xe */ int maxUserNum
  /* this+0x12 */ int userAverageLevel
  /* this+0x16 */ int exp
  /* this+0x1a */ int maxExp
  /* this+0x1e */ int point
  /* this+0x22 */ int honor
  /* this+0x26 */ int virtue
  /* this+0x2a */ int emblemVersion
  /* this+0x2e */ char guildname[24]
  /* this+0x46 */ char masterName[24]
  /* this+0x5e */ char manageLand[16]
  /* this+0x6e */ int zeny
 }

==0x1b7==
 struct PACKET_CZ_GUILD_ZENY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int zeny
 }

==0x1b8==
 struct PACKET_ZC_GUILD_ZENY_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ret
 }

==0x1b9==
 struct PACKET_ZC_DISPEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x1ba==
 struct PACKET_CZ_REMOVE_AID {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char AccountName[24]
 }

==0x1bb==
 struct PACKET_CZ_SHIFT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char CharacterName[24]
 }

==0x1bc==
 struct PACKET_CZ_RECALL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char AccountName[24]
 }

==0x1bd==
 struct PACKET_CZ_RECALL_GID {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char CharacterName[24]
 }

==0x1be==
 struct PACKET_AC_ASK_PNGAMEROOM {
  /* this+0x0 */ short PacketType
 }

==0x1bf==
 struct PACKET_CA_REPLY_PNGAMEROOM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char Permission
 }

==0x1c0==
 struct PACKET_CZ_REQ_REMAINTIME {
  /* this+0x0 */ short PacketType
 }

==0x1c1==
 struct PACKET_ZC_REPLY_REMAINTIME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Result
  /* this+0x6 */ int ExpirationDate
  /* this+0xa */ int RemainTime
 }

==0x1c2==
 struct PACKET_ZC_INFO_REMAINTIME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Type
  /* this+0x6 */ int RemainTime
 }

==0x1c3==
 struct PACKET_ZC_BROADCAST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long fontColor
  /* this+0x8 */ short fontType
  /* this+0xa */ short fontSize
  /* this+0xc */ short fontAlign
  /* this+0xe */ short fontY
  /* this+0x10 */ char msg[...]
 }

==0x1c4==
 struct PACKET_ZC_ADD_ITEM_TO_STORE2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
  /* this+0x8 */ unsigned short ITID
  /* this+0xa */ unsigned char type
  /* this+0xb */ bool IsIdentified
  /* this+0xc */ bool IsDamaged
  /* this+0xd */ unsigned char refiningLevel
  /* this+0xe */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
 }

==0x1c5==
 struct PACKET_ZC_ADD_ITEM_TO_CART2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
  /* this+0x8 */ unsigned short ITID
  /* this+0xa */ unsigned char type
  /* this+0xb */ bool IsIdentified
  /* this+0xc */ bool IsDamaged
  /* this+0xd */ unsigned char refiningLevel
  /* this+0xe */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
 }

==0x1c6==
 struct PACKET_CS_REQ_ENCRYPTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char encCount
  /* this+0x3 */ char decCount
 }

==0x1c7==
 struct PACKET_SC_ACK_ENCRYPTION {
  /* this+0x0 */ short PacketType
 }

==0x1c8==
 struct PACKET_ZC_USE_ITEM_ACK2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ unsigned short id
  /* this+0x6 */ unsigned long AID
  /* this+0xa */ short count
  /* this+0xc */ bool result
 }

==0x1c9==
 struct PACKET_ZC_SKILL_ENTRY2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long creatorAID
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned char job
  /* this+0xf */ bool isVisible
  /* this+0x10 */ bool isContens
  /* this+0x11 */ char msg[80]
 }

==0x1ca==
 struct PACKET_CZ_REQMAKINGHOMUN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool result
 }

==0x1cb==
 struct PACKET_CZ_MONSTER_TALK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char stateId
  /* this+0x7 */ unsigned char skillId
  /* this+0x8 */ unsigned char arg1
 }

==0x1cc==
 struct PACKET_ZC_MONSTER_TALK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char stateId
  /* this+0x7 */ unsigned char skillId
  /* this+0x8 */ unsigned char arg1
 }

==0x1cd==
 struct PACKET_ZC_AUTOSPELLLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int SKID[7]
 }

==0x1ce==
 struct PACKET_CZ_SELECTAUTOSPELL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int SKID
 }

==0x1cf==
 struct PACKET_ZC_DEVOTIONLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long myAID
  /* this+0x6 */ unsigned long AID[5]
  /* this+0x1a */ short range
 }

==0x1d0==
 struct PACKET_ZC_SPIRITS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short num
 }

==0x1d1==
 struct PACKET_ZC_BLADESTOP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long srcAID
  /* this+0x6 */ unsigned long destAID
  /* this+0xa */ int flag
 }

==0x1d2==
 struct PACKET_ZC_COMBODELAY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long delayTime
 }

==0x1d3==
 struct PACKET_ZC_SOUND {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char fileName[24]
  /* this+0x1a */ unsigned char act
  /* this+0x1b */ unsigned long term
  /* this+0x1f */ unsigned long NAID
 }

==0x1d4==
 struct PACKET_ZC_OPEN_EDITDLGSTR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NAID
 }

==0x1d5==
 struct PACKET_CZ_INPUT_EDITDLGSTR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long NAID
  /* this+0x8 */ char msg[...]
 }

==0x1d6==
 struct PACKET_ZC_NOTIFY_MAPPROPERTY2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short type
 }

==0x1d7==
 struct PACKET_ZC_SPRITE_CHANGE2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ int value
 }

==0x1d8==
 struct PACKET_ZC_NOTIFY_STANDENTRY2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ short effectState
  /* this+0xe */ short job
  /* this+0x10 */ short head
  /* this+0x12 */ int weapon
  /* this+0x16 */ short accessory
  /* this+0x18 */ short accessory2
  /* this+0x1a */ short accessory3
  /* this+0x1c */ short headpalette
  /* this+0x1e */ short bodypalette
  /* this+0x20 */ short headDir
  /* this+0x22 */ unsigned long GUID
  /* this+0x26 */ short GEmblemVer
  /* this+0x28 */ short honor
  /* this+0x2a */ short virtue
  /* this+0x2c */ bool isPKModeON
  /* this+0x2d */ unsigned char sex
  /* this+0x2e */ unsigned char PosDir[3]
  /* this+0x31 */ unsigned char xSize
  /* this+0x32 */ unsigned char ySize
  /* this+0x33 */ unsigned char state
  /* this+0x34 */ short clevel
 }

==0x1d9==
 struct PACKET_ZC_NOTIFY_NEWENTRY2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ short effectState
  /* this+0xe */ short job
  /* this+0x10 */ short head
  /* this+0x12 */ int weapon
  /* this+0x16 */ short accessory
  /* this+0x18 */ short accessory2
  /* this+0x1a */ short accessory3
  /* this+0x1c */ short headpalette
  /* this+0x1e */ short bodypalette
  /* this+0x20 */ short headDir
  /* this+0x22 */ unsigned long GUID
  /* this+0x26 */ short GEmblemVer
  /* this+0x28 */ short honor
  /* this+0x2a */ short virtue
  /* this+0x2c */ bool isPKModeON
  /* this+0x2d */ unsigned char sex
  /* this+0x2e */ unsigned char PosDir[3]
  /* this+0x31 */ unsigned char xSize
  /* this+0x32 */ unsigned char ySize
  /* this+0x33 */ short clevel
 }

==0x1da==
 struct PACKET_ZC_NOTIFY_MOVEENTRY2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ short effectState
  /* this+0xe */ short job
  /* this+0x10 */ short head
  /* this+0x12 */ int weapon
  /* this+0x16 */ short accessory
  /* this+0x18 */ unsigned long moveStartTime
  /* this+0x1c */ short accessory2
  /* this+0x1e */ short accessory3
  /* this+0x20 */ short headpalette
  /* this+0x22 */ short bodypalette
  /* this+0x24 */ short headDir
  /* this+0x26 */ unsigned long GUID
  /* this+0x2a */ short GEmblemVer
  /* this+0x2c */ short honor
  /* this+0x2e */ short virtue
  /* this+0x30 */ bool isPKModeON
  /* this+0x31 */ unsigned char sex
  /* this+0x32 */ unsigned char MoveData[6]
  /* this+0x38 */ unsigned char xSize
  /* this+0x39 */ unsigned char ySize
  /* this+0x3a */ short clevel
 }

==0x1db==
 struct PACKET_CA_REQ_HASH {
  /* this+0x0 */ short PacketType
 }

==0x1dc==
 struct PACKET_AC_ACK_HASH {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char secret[...]
 }

==0x1dd==
 struct PACKET_CA_LOGIN2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Version
  /* this+0x6 */ unsigned char ID[24]
  /* this+0x1e */ unsigned char PasswdMD5[16]
  /* this+0x2e */ unsigned char clienttype
 }

==0x1de==
 struct PACKET_ZC_NOTIFY_SKILL2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long targetID
  /* this+0xc */ unsigned long startTime
  /* this+0x10 */ int attackMT
  /* this+0x14 */ int attackedMT
  /* this+0x18 */ int damage
  /* this+0x1c */ short level
  /* this+0x1e */ short count
  /* this+0x20 */ unsigned char action
 }

==0x1df==
 struct PACKET_CZ_REQ_ACCOUNTNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x1e0==
 struct PACKET_ZC_ACK_ACCOUNTNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ char name[24]
 }

==0x1e1==
 struct PACKET_ZC_SPIRITS2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short num
 }

==0x1e2==
 struct PACKET_ZC_REQ_COUPLE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ char name[24]
 }

==0x1e3==
 struct PACKET_CZ_JOIN_COUPLE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ int answer
 }

==0x1e4==
 struct PACKET_ZC_START_COUPLE {
  /* this+0x0 */ short PacketType
 }

==0x1e5==
 struct PACKET_CZ_REQ_JOIN_COUPLE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x1e6==
 struct PACKET_ZC_COUPLENAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char CoupleName[24]
 }

==0x1e7==
 struct PACKET_CZ_DORIDORI {
  /* this+0x0 */ short PacketType
 }

==0x1e8==
 struct PACKET_CZ_MAKE_GROUP2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char groupName[24]
  /* this+0x1a */ unsigned char ItemPickupRule
  /* this+0x1b */ unsigned char ItemDivisionRule
 }

==0x1e9==
 struct PACKET_ZC_ADD_MEMBER_TO_GROUP2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long Role
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned char state
  /* this+0xf */ char groupName[24]
  /* this+0x27 */ char characterName[24]
  /* this+0x3f */ char mapName[16]
  /* this+0x4f */ unsigned char ItemPickupRule
  /* this+0x50 */ unsigned char ItemDivisionRule
 }

==0x1ea==
 struct PACKET_ZC_CONGRATULATION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x1eb==
 struct PACKET_ZC_NOTIFY_POSITION_TO_GUILDM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
 }

==0x1ec==
 struct PACKET_ZC_GUILD_MEMBER_MAP_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GDID
  /* this+0x6 */ unsigned long AID
  /* this+0xa */ char mapName[16]
 }

==0x1ed==
 struct PACKET_CZ_CHOPOKGI {
  /* this+0x0 */ short PacketType
 }

==0x1ee==
 struct PACKET_ZC_NORMAL_ITEMLIST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO2 ItemInfo[...] { // Size 18
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x1ef==
 struct PACKET_ZC_CART_NORMAL_ITEMLIST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO2 ItemInfo[...] { // Size 18
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x1f0==
 struct PACKET_ZC_STORE_NORMAL_ITEMLIST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO2 ItemInfo[...] { // Size 18
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x1f1==
 struct PACKET_AC_NOTIFY_ERROR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x1f2==
 struct PACKET_ZC_UPDATE_CHARSTAT2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ int status
  /* this+0xe */ short sex
  /* this+0x10 */ short head
  /* this+0x12 */ short headPalette
 }

==0x1f3==
 struct PACKET_ZC_NOTIFY_EFFECT2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int effectID
 }

==0x1f4==
 struct PACKET_ZC_REQ_EXCHANGE_ITEM2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
  /* this+0x1a */ unsigned long GID
  /* this+0x1e */ short level
 }

==0x1f5==
 struct PACKET_ZC_ACK_EXCHANGE_ITEM2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char result
  /* this+0x3 */ unsigned long GID
  /* this+0x7 */ short level
 }

==0x1f6==
 struct PACKET_ZC_REQ_BABY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ char name[24]
 }

==0x1f7==
 struct PACKET_CZ_JOIN_BABY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ int answer
 }

==0x1f8==
 struct PACKET_ZC_START_BABY {
  /* this+0x0 */ short PacketType
 }

==0x1f9==
 struct PACKET_CZ_REQ_JOIN_BABY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x1fa==
 struct PACKET_CA_LOGIN3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Version
  /* this+0x6 */ unsigned char ID[24]
  /* this+0x1e */ unsigned char PasswdMD5[16]
  /* this+0x2e */ unsigned char clienttype
  /* this+0x2f */ unsigned char ClientInfo
 }

==0x1fb==
 struct PACKET_CH_DELETE_CHAR2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ char key[50]
 }

==0x1fc==
 struct PACKET_ZC_REPAIRITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct REPAIRITEM_INFO itemList[...] { // Size 13
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char refiningLevel
    /* this+0x5 */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x1fd==
 struct PACKET_CZ_REQ_ITEMREPAIR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct REPAIRITEM_INFO TargetItemInfo {
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char refiningLevel
    /* this+0x5 */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x1fe==
 struct PACKET_ZC_ACK_ITEMREPAIR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ unsigned char result
 }

==0x1ff==
 struct PACKET_ZC_HIGHJUMP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
 }

==0x200==
 struct PACKET_CA_CONNECT_INFO_CHANGED {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ID[24]
 }

==0x201==
 struct PACKET_ZC_FRIENDS_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct STRUCT_FRIEND friendList[...] { // Size 32
    /* this+0x0 */ unsigned long AID
    /* this+0x4 */ unsigned long GID
    /* this+0x8 */ char Name[24]
  }
 }

==0x202==
 struct PACKET_CZ_ADD_FRIENDS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
 }

==0x203==
 struct PACKET_CZ_DELETE_FRIENDS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
 }

==0x204==
 struct PACKET_CA_EXE_HASHCHECK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char HashValue[16]
 }

==0x205==
 struct PACKET_ZC_DIVORCE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
 }

==0x206==
 struct PACKET_ZC_FRIENDS_STATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ bool State
 }

==0x207==
 struct PACKET_ZC_REQ_ADD_FRIENDS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ReqAID
  /* this+0x6 */ unsigned long ReqGID
  /* this+0xa */ char Name[24]
 }

==0x208==
 struct PACKET_CZ_ACK_REQ_ADD_FRIENDS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long ReqAID
  /* this+0x6 */ unsigned long ReqGID
  /* this+0xa */ int Result
 }

==0x209==
 struct PACKET_ZC_ADD_FRIENDS_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long GID
  /* this+0xc */ char Name[24]
 }

==0x20a==
 struct PACKET_ZC_DELETE_FRIENDS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
 }

==0x20b==
 struct PACKET_CH_EXE_HASHCHECK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ClientType
  /* this+0x3 */ unsigned char HashValue[16]
 }

==0x20c==
 struct PACKET_CZ_EXE_HASHCHECK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ClientType
  /* this+0x3 */ unsigned char HashValue[16]
 }

==0x20d==
 struct PACKET_HC_BLOCK_CHARACTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct TAG_CHARACTER_BLOCK_INFO characterList[...] { // Size 24
    /* this+0x0 */ unsigned long GID
    /* this+0x4 */ char szExpireDate[20]
  }
 }

==0x20e==
 struct PACKET_ZC_STARSKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char mapName[24]
  /* this+0x1a */ int monsterID
  /* this+0x1e */ unsigned char star
  /* this+0x1f */ unsigned char result
 }

==0x20f==
 struct PACKET_CZ_REQ_PVPPOINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
 }

==0x210==
 struct PACKET_ZC_ACK_PVPPOINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ struct PVPINFO PVP {
    /* this+0x0 */ int WinPoint
    /* this+0x4 */ int LosePoint
    /* this+0x8 */ int Point
  }
 }

==0x211==
 struct PACKET_ZH_MOVE_PVPWORLD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
 }

==0x212==
 struct PACKET_CZ_REQ_GIVE_MANNER_BYNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char CharName[24]
 }

==0x213==
 struct PACKET_CZ_REQ_STATUS_GM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char CharName[24]
 }

==0x214==
 struct PACKET_ZC_ACK_STATUS_GM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char str
  /* this+0x3 */ unsigned char standardStr
  /* this+0x4 */ unsigned char agi
  /* this+0x5 */ unsigned char standardAgi
  /* this+0x6 */ unsigned char vit
  /* this+0x7 */ unsigned char standardVit
  /* this+0x8 */ unsigned char Int
  /* this+0x9 */ unsigned char standardInt
  /* this+0xa */ unsigned char dex
  /* this+0xb */ unsigned char standardDex
  /* this+0xc */ unsigned char luk
  /* this+0xd */ unsigned char standardLuk
  /* this+0xe */ short attPower
  /* this+0x10 */ short refiningPower
  /* this+0x12 */ short max_mattPower
  /* this+0x14 */ short min_mattPower
  /* this+0x16 */ short itemdefPower
  /* this+0x18 */ short plusdefPower
  /* this+0x1a */ short mdefPower
  /* this+0x1c */ short plusmdefPower
  /* this+0x1e */ short hitSuccessValue
  /* this+0x20 */ short avoidSuccessValue
  /* this+0x22 */ short plusAvoidSuccessValue
  /* this+0x24 */ short criticalSuccessValue
  /* this+0x26 */ short ASPD
  /* this+0x28 */ short plusASPD
 }

==0x215==
 struct PACKET_ZC_SKILLMSG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MsgNo
 }

==0x216==
 struct PACKET_ZC_BABYMSG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MsgNo
 }

==0x217==
 struct PACKET_CZ_BLACKSMITH_RANK {
  /* this+0x0 */ short PacketType
 }

==0x218==
 struct PACKET_CZ_ALCHEMIST_RANK {
  /* this+0x0 */ short PacketType
 }

==0x219==
 struct PACKET_ZC_BLACKSMITH_RANK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Name[10][24]
  /* this+0xf2 */ int Point[10]
 }

==0x21a==
 struct PACKET_ZC_ALCHEMIST_RANK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Name[10][24]
  /* this+0xf2 */ int Point[10]
 }

==0x21b==
 struct PACKET_ZC_BLACKSMITH_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Point
  /* this+0x6 */ int TotalPoint
 }

==0x21c==
 struct PACKET_ZC_ALCHEMIST_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Point
  /* this+0x6 */ int TotalPoint
 }

==0x21d==
 struct PACKET_CZ_LESSEFFECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int isLess
 }

==0x21e==
 struct PACKET_ZC_LESSEFFECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int isLess
 }

==0x21f==
 struct PACKET_ZC_NOTIFY_PKINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int winPoint
  /* this+0x6 */ int losePoint
  /* this+0xa */ char killName[24]
  /* this+0x22 */ char killedName[24]
  /* this+0x3a */ struct _FILETIME expireTime {
    /* this+0x0 */ unsigned long dwLowDateTime
    /* this+0x4 */ unsigned long dwHighDateTime
  }
 }

==0x220==
 struct PACKET_ZC_NOTIFY_CRAZYKILLER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int isCrazyKiller
 }

==0x221==
 struct PACKET_ZC_NOTIFY_WEAPONITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct REPAIRITEM_INFO itemList[...] { // Size 13
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char refiningLevel
    /* this+0x5 */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x222==
 struct PACKET_CZ_REQ_WEAPONREFINE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Index
 }

==0x223==
 struct PACKET_ZC_ACK_WEAPONREFINE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int msg
  /* this+0x6 */ unsigned short ITID
 }

==0x224==
 struct PACKET_ZC_TAEKWON_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Point
  /* this+0x6 */ int TotalPoint
 }

==0x225==
 struct PACKET_CZ_TAEKWON_RANK {
  /* this+0x0 */ short PacketType
 }

==0x226==
 struct PACKET_ZC_TAEKWON_RANK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Name[10][24]
  /* this+0xf2 */ int Point[10]
 }

==0x227==
 struct PACKET_ZC_GAME_GUARD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuthData[4]
 }

==0x228==
 struct PACKET_CZ_ACK_GAME_GUARD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuthData[4]
 }

==0x229==
 struct PACKET_ZC_STATE_CHANGE3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short bodyState
  /* this+0x8 */ short healthState
  /* this+0xa */ int effectState
  /* this+0xe */ bool isPKModeON
 }

==0x22a==
 struct PACKET_ZC_NOTIFY_STANDENTRY3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ int effectState
  /* this+0x10 */ short job
  /* this+0x12 */ short head
  /* this+0x14 */ int weapon
  /* this+0x18 */ short accessory
  /* this+0x1a */ short accessory2
  /* this+0x1c */ short accessory3
  /* this+0x1e */ short headpalette
  /* this+0x20 */ short bodypalette
  /* this+0x22 */ short headDir
  /* this+0x24 */ unsigned long GUID
  /* this+0x28 */ short GEmblemVer
  /* this+0x2a */ short honor
  /* this+0x2c */ int virtue
  /* this+0x30 */ bool isPKModeON
  /* this+0x31 */ unsigned char sex
  /* this+0x32 */ unsigned char PosDir[3]
  /* this+0x35 */ unsigned char xSize
  /* this+0x36 */ unsigned char ySize
  /* this+0x37 */ unsigned char state
  /* this+0x38 */ short clevel
 }

==0x22b==
 struct PACKET_ZC_NOTIFY_NEWENTRY3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ int effectState
  /* this+0x10 */ short job
  /* this+0x12 */ short head
  /* this+0x14 */ int weapon
  /* this+0x18 */ short accessory
  /* this+0x1a */ short accessory2
  /* this+0x1c */ short accessory3
  /* this+0x1e */ short headpalette
  /* this+0x20 */ short bodypalette
  /* this+0x22 */ short headDir
  /* this+0x24 */ unsigned long GUID
  /* this+0x28 */ short GEmblemVer
  /* this+0x2a */ short honor
  /* this+0x2c */ int virtue
  /* this+0x30 */ bool isPKModeON
  /* this+0x31 */ unsigned char sex
  /* this+0x32 */ unsigned char PosDir[3]
  /* this+0x35 */ unsigned char xSize
  /* this+0x36 */ unsigned char ySize
  /* this+0x37 */ short clevel
 }

==0x22c==
 struct PACKET_ZC_NOTIFY_MOVEENTRY3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char objecttype
  /* this+0x3 */ unsigned long GID
  /* this+0x7 */ short speed
  /* this+0x9 */ short bodyState
  /* this+0xb */ short healthState
  /* this+0xd */ int effectState
  /* this+0x11 */ short job
  /* this+0x13 */ short head
  /* this+0x15 */ int weapon
  /* this+0x19 */ short accessory
  /* this+0x1b */ unsigned long moveStartTime
  /* this+0x1f */ short accessory2
  /* this+0x21 */ short accessory3
  /* this+0x23 */ short headpalette
  /* this+0x25 */ short bodypalette
  /* this+0x27 */ short headDir
  /* this+0x29 */ unsigned long GUID
  /* this+0x2d */ short GEmblemVer
  /* this+0x2f */ short honor
  /* this+0x31 */ int virtue
  /* this+0x35 */ bool isPKModeON
  /* this+0x36 */ unsigned char sex
  /* this+0x37 */ unsigned char MoveData[6]
  /* this+0x3d */ unsigned char xSize
  /* this+0x3e */ unsigned char ySize
  /* this+0x3f */ short clevel
 }

==0x22d==
 struct PACKET_CZ_COMMAND_MER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short type
  /* this+0x4 */ char command
 }

==0x22e==
 struct PACKET_ZC_PROPERTY_HOMUN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char szName[24]
  /* this+0x1a */ unsigned char bModified
  /* this+0x1b */ short nLevel
  /* this+0x1d */ short nFullness
  /* this+0x1f */ short nRelationship
  /* this+0x21 */ unsigned short ITID
  /* this+0x23 */ short atk
  /* this+0x25 */ short Matk
  /* this+0x27 */ short hit
  /* this+0x29 */ short critical
  /* this+0x2b */ short def
  /* this+0x2d */ short Mdef
  /* this+0x2f */ short flee
  /* this+0x31 */ short aspd
  /* this+0x33 */ short hp
  /* this+0x35 */ short maxHP
  /* this+0x37 */ short sp
  /* this+0x39 */ short maxSP
  /* this+0x3b */ int exp
  /* this+0x3f */ int maxEXP
  /* this+0x43 */ short SKPoint
  /* this+0x45 */ short ATKRange
 }

==0x230==
 struct PACKET_ZC_CHANGESTATE_MER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char type
  /* this+0x3 */ char state
  /* this+0x4 */ int GID
  /* this+0x8 */ int data
 }

==0x231==
 struct PACKET_CZ_RENAME_MER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
 }

==0x232==
 struct PACKET_CZ_REQUEST_MOVENPC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char dest[3]
 }

==0x233==
 struct PACKET_CZ_REQUEST_ACTNPC {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned long targetGID
  /* this+0xa */ unsigned char action
 }

==0x234==
 struct PACKET_CZ_REQUEST_MOVETOOWNER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
 }

==0x23a==
 struct PACKET_ZC_REQ_STORE_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Info
 }

==0x23b==
 struct PACKET_CZ_ACK_STORE_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Type
  /* this+0x4 */ unsigned char Password[16]
  /* this+0x14 */ unsigned char NewPassword[16]
 }

==0x23c==
 struct PACKET_ZC_RESULT_STORE_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ short ErrorCount
 }

==0x23d==
 struct PACKET_AC_EVENT_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long EventItemCount
 }

==0x23e==
 struct PACKET_HC_REQUEST_CHARACTER_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ unsigned long dummyValue
 }

==0x23f==
 struct PACKET_CZ_MAIL_GET_LIST {
  /* this+0x0 */ short PacketType
 }

==0x240==
 struct PACKET_ZC_MAIL_REQ_GET_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int MailNumber
  /* this+0x8 */ struct MAIL_LIST mailList[...] { // Size 73
    /* this+0x0 */ unsigned long MailID
    /* this+0x4 */ char HEADER[40]
    /* this+0x2c */ char isOpen
    /* this+0x2d */ char FromName[24]
    /* this+0x45 */ long DeleteTime
  }
 }

==0x241==
 struct PACKET_CZ_MAIL_OPEN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MailID
 }

==0x242==
 struct PACKET_ZC_MAIL_REQ_OPEN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int MailID
  /* this+0x8 */ char Header[40]
  /* this+0x30 */ char FromName[24]
  /* this+0x48 */ long DeleteTime
  /* this+0x4c */ unsigned long Money
  /* this+0x50 */ int count
  /* this+0x54 */ unsigned short ITID
  /* this+0x56 */ unsigned short Type
  /* this+0x58 */ bool IsIdentified
  /* this+0x59 */ bool IsDamaged
  /* this+0x5a */ unsigned char refiningLevel
  /* this+0x5b */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
  /* this+0x63 */ unsigned char msg_len
  /* this+0x64 */ char msg[...]
 }

==0x243==
 struct PACKET_CZ_MAIL_DELETE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MailID
 }

==0x244==
 struct PACKET_CZ_MAIL_GET_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MailID
 }

==0x245==
 struct PACKET_ZC_MAIL_REQ_GET_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Result
 }

==0x246==
 struct PACKET_CZ_MAIL_RESET_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Type
 }

==0x247==
 struct PACKET_CZ_MAIL_ADD_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x248==
 struct PACKET_CZ_MAIL_SEND {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char ReceiveName[24]
  /* this+0x1c */ char Header[40]
  /* this+0x44 */ unsigned long msg_len
  /* this+0x48 */ char msg[...]
 }

==0x249==
 struct PACKET_ZC_MAIL_REQ_SEND {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Result
 }

==0x24a==
 struct PACKET_ZC_MAIL_RECEIVE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long MailID
  /* this+0x6 */ char Header[40]
  /* this+0x2e */ char FromName[24]
 }

==0x24b==
 struct PACKET_CZ_AUCTION_CREATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Type
 }

==0x24c==
 struct PACKET_CZ_AUCTION_ADD_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x24d==
 struct PACKET_CZ_AUCTION_ADD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long NowMoney
  /* this+0x6 */ unsigned long MaxMoney
  /* this+0xa */ short DeleteHour
 }

==0x24e==
 struct PACKET_CZ_AUCTION_ADD_CANCEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuctionID
 }

==0x24f==
 struct PACKET_CZ_AUCTION_BUY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuctionID
  /* this+0x6 */ unsigned long Money
 }

==0x250==
 struct PACKET_ZC_AUCTION_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Result
 }

==0x251==
 struct PACKET_CZ_AUCTION_ITEM_SEARCH {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Type
  /* this+0x4 */ unsigned long AuctionID
  /* this+0x8 */ char Name[24]
  /* this+0x20 */ unsigned short Page
 }

==0x252==
 struct PACKET_ZC_AUCTION_ITEM_REQ_SEARCH {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int MaxPage
  /* this+0x8 */ int Number
  /* this+0xc */ struct AUCTION_ITEM_SEARCH_INFO auctionItemList[...] { // Size 83
    /* this+0x0 */ unsigned long AuctionID
    /* this+0x4 */ char SellerName[24]
    /* this+0x1c */ unsigned short ITID
    /* this+0x1e */ int Type
    /* this+0x22 */ short count
    /* this+0x24 */ bool IsIdentified
    /* this+0x25 */ bool IsDamaged
    /* this+0x26 */ unsigned char refiningLevel
    /* this+0x27 */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x2f */ int NowPrice
    /* this+0x33 */ int MaxPrice
    /* this+0x37 */ char BuyerName[24]
    /* this+0x4f */ long DeleteTime
  }
 }

==0x253==
 struct PACKET_ZC_STARPLACE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char which
 }

==0x254==
 struct PACKET_CZ_AGREE_STARPLACE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char which
 }

==0x255==
 struct PACKET_ZC_ACK_MAIL_ADD_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Index
  /* this+0x4 */ unsigned char result
 }

==0x256==
 struct PACKET_ZC_ACK_AUCTION_ADD_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Index
  /* this+0x4 */ unsigned char result
 }

==0x257==
 struct PACKET_ZC_ACK_MAIL_DELETE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MailID
  /* this+0x6 */ unsigned short Result
 }

==0x258==
 struct PACKET_CA_REQ_GAME_GUARD_CHECK {
  /* this+0x0 */ short PacketType
 }

==0x259==
 struct PACKET_AC_ACK_GAME_GUARD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ucAnswer
 }

==0x25a==
 struct PACKET_ZC_MAKINGITEM_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned short idList[...]
 }

==0x25b==
 struct PACKET_CZ_REQ_MAKINGITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short mkType
  /* this+0x4 */ unsigned short id
 }

==0x25c==
 struct PACKET_CZ_AUCTION_REQ_MY_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Type
 }

==0x25d==
 struct PACKET_CZ_AUCTION_REQ_MY_SELL_STOP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuctionID
 }

==0x25e==
 struct PACKET_ZC_AUCTION_ACK_MY_SELL_STOP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
 }

==0x25f==
 struct PACKET_ZC_AUCTION_WINDOWS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Type
 }

==0x260==
 struct PACKET_ZC_MAIL_WINDOWS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Type
 }

==0x261==
 struct PACKET_AC_REQ_LOGIN_OLDEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char m_SeedValue[9]
 }

==0x262==
 struct PACKET_AC_REQ_LOGIN_NEWEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char m_SeedValue[9]
 }

==0x263==
 struct PACKET_AC_REQ_LOGIN_CARDPASS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char m_SeedValue[9]
 }

==0x264==
 struct PACKET_CA_ACK_LOGIN_OLDEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char m_SeedValue[9]
  /* this+0xb */ char m_EKey[9]
 }

==0x265==
 struct PACKET_CA_ACK_LOGIN_NEWEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char m_SeedValue[9]
  /* this+0xb */ char m_EKey[9]
 }

==0x266==
 struct PACKET_CA_ACK_LOGIN_CARDPASS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char m_cardPass[28]
 }

==0x267==
 struct PACKET_AC_ACK_EKEY_FAIL_NOTEXIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x268==
 struct PACKET_AC_ACK_EKEY_FAIL_NOTUSESEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x269==
 struct PACKET_AC_ACK_EKEY_FAIL_NOTUSEDEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x26a==
 struct PACKET_AC_ACK_EKEY_FAIL_AUTHREFUSE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x26b==
 struct PACKET_AC_ACK_EKEY_FAIL_INPUTEKEY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x26c==
 struct PACKET_AC_ACK_EKEY_FAIL_NOTICE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x26d==
 struct PACKET_AC_ACK_EKEY_FAIL_NEEDCARDPASS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x26e==
 struct PACKET_AC_ACK_AUTHEKEY_FAIL_NOTMATCHCARDPASS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short errorCode
 }

==0x26f==
 struct PACKET_AC_ACK_FIRST_LOGIN {
  /* this+0x0 */ short PacketType
 }

==0x270==
 struct PACKET_AC_REQ_LOGIN_ACCOUNT_INFO {
  /* this+0x0 */ short PacketType
 }

==0x271==
 struct PACKET_CA_ACK_LOGIN_ACCOUNT_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short sex
  /* this+0x4 */ short bPoint
  /* this+0x6 */ char E_mail[34]
 }

==0x272==
 struct PACKET_AC_ACK_PT_ID_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char szPTID[21]
  /* this+0x17 */ char szPTNumID[21]
 }

==0x273==
 struct PACKET_CZ_REQ_MAIL_RETURN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MailID
  /* this+0x6 */ char ReceiveName[24]
 }

==0x274==
 struct PACKET_ZC_ACK_MAIL_RETURN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int MailID
  /* this+0x6 */ short Result
 }

==0x275==
 struct PACKET_CH_ENTER2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int AuthCode
  /* this+0xa */ unsigned long userLevel
  /* this+0xe */ unsigned short clientType
  /* this+0x10 */ unsigned char Sex
  /* this+0x11 */ char macData[16]
  /* this+0x21 */ int iAccountSID
 }

==0x276==
 struct PACKET_AC_ACCEPT_LOGIN2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int AuthCode
  /* this+0x8 */ unsigned long AID
  /* this+0xc */ unsigned long userLevel
  /* this+0x10 */ unsigned long lastLoginIP
  /* this+0x14 */ char lastLoginTime[26]
  /* this+0x2e */ unsigned char Sex
  /* this+0x2f */ int iAccountSID
 }

==0x277==
 struct PACKET_CA_LOGIN_PCBANG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Version
  /* this+0x6 */ unsigned char ID[24]
  /* this+0x1e */ unsigned char Passwd[24]
  /* this+0x36 */ unsigned char clienttype
  /* this+0x37 */ char IP[16]
  /* this+0x47 */ unsigned char MacAdress[13]
 }

==0x278==
 struct PACKET_ZC_NOTIFY_PCBANG {
  /* this+0x0 */ short PacketType
 }

==0x279==
 struct PACKET_CZ_HUNTINGLIST {
  /* this+0x0 */ short PacketType
 }

==0x27a==
 struct PACKET_ZC_HUNTINGLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */  struct PACKET_MOB_HUNTING HuntingList[...] { // Size 12
    /* this+0x0 */ unsigned long questID
    /* this+0x4 */ unsigned long mobGID
    /* this+0x8 */ short maxCount
    /* this+0xa */ short count
  }
 }

==0x27b==
 struct PACKET_ZC_PCBANG_EFFECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int ExpFactor
  /* this+0x6 */ int ExpFactor2
  /* this+0xa */ int DropFactor
 }

==0x27c==
 struct PACKET_CA_LOGIN4 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Version
  /* this+0x6 */ unsigned char ID[24]
  /* this+0x1e */ unsigned char PasswdMD5[16]
  /* this+0x2e */ unsigned char clienttype
  /* this+0x2f */ char macData[13]
 }

==0x27d==
 struct PACKET_ZC_PROPERTY_MERCE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char name[24]
  /* this+0x1a */ short level
  /* this+0x1c */ short faith
  /* this+0x1e */ short summonCount
  /* this+0x20 */ short atk
  /* this+0x22 */ short Matk
  /* this+0x24 */ short hit
  /* this+0x26 */ short critical
  /* this+0x28 */ short def
  /* this+0x2a */ short Mdef
  /* this+0x2c */ short flee
  /* this+0x2e */ short aspd
  /* this+0x30 */ short hp
  /* this+0x32 */ short maxHP
  /* this+0x34 */ short sp
  /* this+0x36 */ short maxSP
  /* this+0x38 */ short ATKRange
  /* this+0x3a */ int exp
 }

==0x27e==
 struct PACKET_ZC_SHANDA_PROTECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short CodeLen
  /* this+0x6 */ unsigned char Code[...]
 }

==0x27f==
 struct PACKET_CA_CLIENT_TYPE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short ClientType
  /* this+0x4 */ int nVer
 }

==0x280==
 struct PACKET_ZC_GANGSI_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int Point
  /* this+0x6 */ int TotalPoint
  /* this+0xa */ short PacketSwitch
 }

==0x281==
 struct PACKET_CZ_GANGSI_RANK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketSwitch
 }

==0x282==
 struct PACKET_ZC_GANGSI_RANK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Name[10][24]
  /* this+0xf2 */ int Point[10]
  /* this+0x11a */ short PacketSwitch
 }

==0x283==
 struct PACKET_ZC_AID {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x284==
 struct PACKET_ZC_NOTIFY_EFFECT3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int effectID
  /* this+0xa */ int numdata
 }

==0x285==
 struct PACKET_ZC_DEATH_QUESTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Qcategory
  /* this+0x4 */ short Qnum
 }

==0x286==
 struct PACKET_CZ_DEATH_QUESTION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Qanswer
 }

==0x287==
 struct PACKET_ZC_PC_CASH_POINT_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long CashPoint
  /* this+0x8 */ struct PURCHASE_ITEM itemList[...] { // Size 11
    /* this+0x0 */ int price
    /* this+0x4 */ int discountprice
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
  }
 }

==0x288==
 struct PACKET_CZ_PC_BUY_CASH_POINT_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ITID
  /* this+0x4 */ short count
 }

==0x289==
 struct PACKET_ZC_PC_CASH_POINT_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long CashPoint
  /* this+0x6 */ short Error
 }

==0x28a==
 struct PACKET_ZC_NPC_SHOWEFST_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int effectState
  /* this+0xa */ int clevel
  /* this+0xe */ int showEFST
 }

==0x28c==
 struct PACKET_CH_SELECT_CHAR_GOINGTOBEUSED {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long dwAID
  /* this+0x6 */ int nCountSelectedChar
  /* this+0xa */ unsigned long ardwSelectedGID[9]
 }

==0x28d==
 struct PACKET_CH_REQ_IS_VALID_CHARNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long dwAID
  /* this+0x6 */ unsigned long dwGID
  /* this+0xa */ char szCharName[24]
 }

==0x28e==
 struct PACKET_HC_ACK_IS_VALID_CHARNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short sResult
 }

==0x28f==
 struct PACKET_CH_REQ_CHANGE_CHARNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long dwGID
 }

==0x290==
 struct PACKET_HC_ACK_CHANGE_CHARNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short sResult
 }

==0x291==
 struct PACKET_ZC_MSG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short msg
 }

==0x292==
 struct PACKET_CZ_STANDING_RESURRECTION {
  /* this+0x0 */ short PacketType
 }

==0x293==
 struct PACKET_ZC_BOSS_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char infoType
  /* this+0x3 */ int xPos
  /* this+0x7 */ int yPos
  /* this+0xb */ unsigned short minHour
  /* this+0xd */ unsigned short minMinute
  /* this+0xf */ unsigned short maxHour
  /* this+0x11 */ unsigned short maxMinute
  /* this+0x13 */ char name[51]
 }

==0x294==
 struct PACKET_ZC_READ_BOOK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long bookID
  /* this+0x6 */ unsigned long page
 }

==0x295==
 struct PACKET_ZC_EQUIPMENT_ITEMLIST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO2 ItemInfo[...] { // Size 24
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
  }
 }

==0x296==
 struct PACKET_ZC_STORE_EQUIPMENT_ITEMLIST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO2 ItemInfo[...] { // Size 24
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
  }
 }

==0x297==
 struct PACKET_ZC_CART_EQUIPMENT_ITEMLIST2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO2 ItemInfo[...] { // Size 24
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
  }
 }

==0x298==
 struct PACKET_ZC_CASH_TIME_COUNTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ITID
  /* this+0x4 */ unsigned long RemainSecond
 }

==0x299==
 struct PACKET_ZC_CASH_ITEM_DELETE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ unsigned short ITID
 }

==0x29a==
 struct PACKET_ZC_ITEM_PICKUP_ACK2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Index
  /* this+0x4 */ unsigned short count
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ bool IsDamaged
  /* this+0xa */ unsigned char refiningLevel
  /* this+0xb */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
  /* this+0x13 */ unsigned short location
  /* this+0x15 */ unsigned char type
  /* this+0x16 */ unsigned char result
  /* this+0x17 */ long HireExpireDate
 }

==0x29b==
 struct PACKET_ZC_MER_INIT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int AID
  /* this+0x6 */ short atk
  /* this+0x8 */ short Matk
  /* this+0xa */ short hit
  /* this+0xc */ short critical
  /* this+0xe */ short def
  /* this+0x10 */ short Mdef
  /* this+0x12 */ short flee
  /* this+0x14 */ short aspd
  /* this+0x16 */ char name[24]
  /* this+0x2e */ short level
  /* this+0x30 */ int hp
  /* this+0x34 */ int maxHP
  /* this+0x38 */ int sp
  /* this+0x3c */ int maxSP
  /* this+0x40 */ long ExpireDate
  /* this+0x44 */ short faith
  /* this+0x46 */ int toal_call_num
  /* this+0x4a */ int approval_monster_kill_counter
  /* this+0x4e */ short ATKRange
 }

==0x29c==
 struct PACKET_ZC_MER_PROPERTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short atk
  /* this+0x4 */ short Matk
  /* this+0x6 */ short hit
  /* this+0x8 */ short critical
  /* this+0xa */ short def
  /* this+0xc */ short Mdef
  /* this+0xe */ short flee
  /* this+0x10 */ short aspd
  /* this+0x12 */ char name[24]
  /* this+0x2a */ short level
  /* this+0x2c */ short hp
  /* this+0x2e */ short maxHP
  /* this+0x30 */ short sp
  /* this+0x32 */ short maxSP
  /* this+0x34 */ long ExpireDate
  /* this+0x38 */ short faith
  /* this+0x3a */ int toal_call_num
  /* this+0x3e */ int approval_monster_kill_counter
 }

==0x29d==
 struct PACKET_ZC_MER_SKILLINFO_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct SKILLINFO skillList[...] { // Size 37
    /* this+0x0 */ short SKID
    /* this+0x2 */ int type
    /* this+0x6 */ short level
    /* this+0x8 */ short spcost
    /* this+0xa */ short attackRange
    /* this+0xc */ unsigned char skillName[24]
    /* this+0x24 */ char upgradable
  }
 }

==0x29e==
 struct PACKET_ZC_MER_SKILLINFO_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ short level
  /* this+0x6 */ short spcost
  /* this+0x8 */ short attackRange
  /* this+0xa */ bool upgradable
 }

==0x29f==
 struct PACKET_CZ_MER_COMMAND {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char command
 }

==0x2a0==
struct UNUSED_PACKET_CZ_MER_USE_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short selectedLevel
  /* this+0x4 */ unsigned short SKID
  /* this+0x6 */ unsigned long targetID
 }

==0x2a1==
struct UNUSED_PACKET_CZ_MER_UPGRADE_SKILLLEVEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
 }

==0x2a2==
 struct PACKET_ZC_MER_PAR_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short var
  /* this+0x4 */ int value
 }

==0x2a3==
 struct PACKET_ZC_GAMEGUARD_LINGO_KEY {
  /* this+0x0 */ short packetType
  /* this+0x2 */ struct PGG_LINGO_KEY_TEMP lingoKey {
    /* this+0x0 */ unsigned long dwAlgNum
    /* this+0x4 */ unsigned long dwAlgKey1
    /* this+0x8 */ unsigned long dwAlgKey2
    /* this+0xc */ unsigned long dwSeed
  }
 }

==0x2a5==
 struct PACKET_CZ_KSY_EVENT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ int count
 }

==0x2aa==
 struct PACKET_ZC_REQ_CASH_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Info
 }

==0x2ab==
 struct PACKET_CZ_ACK_CASH_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Type
  /* this+0x4 */ unsigned char Password[16]
  /* this+0x14 */ unsigned char NewPassword[16]
 }

==0x2ac==
 struct PACKET_ZC_RESULT_CASH_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ short ErrorCount
 }

==0x2ad==
 struct PACKET_AC_REQUEST_SECOND_PASSWORD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ unsigned long dwSeed
 }

==0x2b0==
 struct PACKET_CA_LOGIN_HAN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Version
  /* this+0x6 */ unsigned char ID[24]
  /* this+0x1e */ unsigned char Passwd[24]
  /* this+0x36 */ unsigned char clienttype
  /* this+0x37 */ char m_szIP[16]
  /* this+0x47 */ unsigned char m_szMacAddr[13]
  /* this+0x54 */ unsigned char isHanGameUser
 }

==0x2b1==
 struct PACKET_ZC_ALL_QUEST_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int questCount
  /* this+0x8 */  struct PACKET_ZC_QUEST_INFO QuestList[...] { // Size 5
    /* this+0x0 */ unsigned long questID
    /* this+0x4 */ bool active
  }
 }

==0x2b2==
 struct PACKET_ZC_ALL_QUEST_MISSION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int count
  /* this+0x8 */  struct PACKET_ZC_QUEST_MISSION_INFO QuestMissionList[...] { // Size 104
    /* this+0x0 */ unsigned long questID
    /* this+0x4 */ long quest_svrTime
    /* this+0x8 */ long quest_endTime
    /* this+0xc */ short count
    /* this+0xe */  struct PACKET_ZC_MISSION_HUNT hunt[3] { // Size 30
      /* this+0x0 */ unsigned long mobGID
      /* this+0x4 */ short huntCount
      /* this+0x6 */ char mobName[24]
    }
  }
 }

==0x2b3==
 struct PACKET_ZC_ADD_QUEST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long questID
  /* this+0x6 */ bool active
  /* this+0x7 */ long quest_svrTime
  /* this+0xb */ long quest_endTime
  /* this+0xf */ short count
  /* this+0x11 */  struct PACKET_ZC_MISSION_HUNT hunt[3] { // Size 30
    /* this+0x0 */ unsigned long mobGID
    /* this+0x4 */ short huntCount
    /* this+0x6 */ char mobName[24]
  }
 }

==0x2b4==
 struct PACKET_ZC_DEL_QUEST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long questID
 }

==0x2b5==
 struct PACKET_ZC_UPDATE_MISSION_HUNT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short count
  /* this+0x6 */  struct PACKET_MOB_HUNTING MobHuntList[...] { // Size 12
    /* this+0x0 */ unsigned long questID
    /* this+0x4 */ unsigned long mobGID
    /* this+0x8 */ short maxCount
    /* this+0xa */ short count
  }
 }

==0x2b6==
 struct PACKET_CZ_ACTIVE_QUEST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long questID
  /* this+0x6 */ bool active
 }

==0x2b7==
 struct PACKET_ZC_ACTIVE_QUEST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long questID
  /* this+0x6 */ bool active
 }

==0x2b8==
 struct PACKET_ZC_ITEM_PICKUP_PARTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long accountID
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ bool IsDamaged
  /* this+0xa */ unsigned char refiningLevel
  /* this+0xb */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
  /* this+0x13 */ unsigned short location
  /* this+0x15 */ unsigned char type
 }

==0x2b9==
 struct PACKET_ZC_SHORTCUT_KEY_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct ShortCutKey ShortCutKey[27] { // Size 7
    /* this+0x0 */ char isSkill
    /* this+0x1 */ unsigned long ID
    /* this+0x5 */ short count
  }
 }

==0x2ba==
 struct PACKET_CZ_SHORTCUT_KEY_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Index
  /* this+0x4 */ struct ShortCutKey ShortCutKey {
    /* this+0x0 */ char isSkill
    /* this+0x1 */ unsigned long ID
    /* this+0x5 */ short count
  }
 }

==0x2bb==
 struct PACKET_ZC_EQUIPITEM_DAMAGED {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short wearLocation
  /* this+0x4 */ unsigned long accountID
 }

==0x2bc==
 struct PACKET_ZC_NOTIFY_PCBANG_PLAYING_TIME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int TimeMinute
 }

==0x2bf==
 struct PACKET_ZC_SRPACKETR2_INIT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ProtectFactor
  /* this+0x4 */ unsigned int DeformSeedFactor
  /* this+0x8 */ unsigned int DeformAddFactor
 }

==0x2c0==
 struct PACKET_CZ_SRPACKETR2_START {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ProtectFactor
 }

==0x2c1==
 struct PACKET_ZC_NPC_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long accountID
  /* this+0x8 */ unsigned long color
  /* this+0xc */ char msg[...]
 }

==0x2c2==
 struct PACKET_ZC_FORMATSTRING_MSG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned short msg
  /* this+0x6 */ char value[...]
 }

==0x2c4==
 struct PACKET_CZ_PARTY_JOIN_REQ {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char characterName[24]
 }

==0x2c5==
 struct PACKET_ZC_PARTY_JOIN_REQ_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char characterName[24]
  /* this+0x1a */ long answer
 }

==0x2c6==
 struct PACKET_ZC_PARTY_JOIN_REQ {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GRID
  /* this+0x6 */ char groupName[24]
 }

==0x2c7==
 struct PACKET_CZ_PARTY_JOIN_REQ_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GRID
  /* this+0x6 */ bool bAccept
 }

==0x2c8==
 struct PACKET_CZ_PARTY_CONFIG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool bRefuseJoinMsg
 }

==0x2c9==
 struct PACKET_ZC_PARTY_CONFIG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool bRefuseJoinMsg
 }

==0x2ca==
 struct PACKET_HC_REFUSE_SELECTCHAR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char ErrorCode
 }

==0x2cb==
 struct PACKET_ZC_MEMORIALDUNGEON_SUBSCRIPTION_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char MemorialDungeonName[61]
  /* this+0x3f */ short PriorityOrderNum
 }

==0x2cc==
 struct PACKET_ZC_MEMORIALDUNGEON_SUBSCRIPTION_NOTIFY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PriorityOrderNum
 }

==0x2cd==
 struct PACKET_ZC_MEMORIALDUNGEON_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char MemorialDungeonName[61]
  /* this+0x3f */ unsigned long DestroyDate
  /* this+0x43 */ unsigned long EnterTimeOutDate
 }

==0x2ce==
 struct PACKET_ZC_MEMORIALDUNGEON_NOTIFY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long Type
  /* this+0x6 */ unsigned long EnterLimitDate
 }

==0x2cf==
 struct PACKET_CZ_MEMORIALDUNGEON_COMMAND {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long Command
 }

==0x2d0==
 struct PACKET_ZC_EQUIPMENT_ITEMLIST3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO301 ItemInfo[...] { // Size 28
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
    /* this+0x18 */ unsigned short bindOnEquipType
    /* this+0x1a */ unsigned short wItemSpriteNumber
  }
 }

==0x2d1==
 struct PACKET_ZC_STORE_EQUIPMENT_ITEMLIST3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO301 ItemInfo[...] { // Size 28
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
    /* this+0x18 */ unsigned short bindOnEquipType
    /* this+0x1a */ unsigned short wItemSpriteNumber
  }
 }

==0x2d2==
 struct PACKET_ZC_CART_EQUIPMENT_ITEMLIST3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct EQUIPMENTITEM_EXTRAINFO301 ItemInfo[...] { // Size 28
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
    /* this+0x18 */ unsigned short bindOnEquipType
    /* this+0x1a */ unsigned short wItemSpriteNumber
  }
 }

==0x2d3==
 struct PACKET_ZC_NOTIFY_BIND_ON_EQUIP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
 }

==0x2d4==
 struct PACKET_ZC_ITEM_PICKUP_ACK3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Index
  /* this+0x4 */ unsigned short count
  /* this+0x6 */ unsigned short ITID
  /* this+0x8 */ bool IsIdentified
  /* this+0x9 */ bool IsDamaged
  /* this+0xa */ unsigned char refiningLevel
  /* this+0xb */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
  /* this+0x13 */ unsigned short location
  /* this+0x15 */ unsigned char type
  /* this+0x16 */ unsigned char result
  /* this+0x17 */ long HireExpireDate
  /* this+0x1b */ unsigned short bindOnEquipType
 }

==0x2d5==
 struct PACKET_ZC_ISVR_DISCONNECT {
  /* this+0x0 */ short PacketType
 }

==0x2d6==
 struct PACKET_CZ_EQUIPWIN_MICROSCOPE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x2d7==
 struct PACKET_ZC_EQUIPWIN_MICROSCOPE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char characterName[24]
  /* this+0x1c */ short job
  /* this+0x1e */ short head
  /* this+0x20 */ short accessory
  /* this+0x22 */ short accessory2
  /* this+0x24 */ short accessory3
  /* this+0x26 */ short headpalette
  /* this+0x28 */ short bodypalette
  /* this+0x2a */ unsigned char sex
  /* this+0x2b */ struct EQUIPMENTITEM_EXTRAINFO301 ItemInfo[...] { // Size 28
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ unsigned short location
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ bool IsDamaged
    /* this+0xb */ unsigned char RefiningLevel
    /* this+0xc */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x14 */ long HireExpireDate
    /* this+0x18 */ unsigned short bindOnEquipType
    /* this+0x1a */ unsigned short wItemSpriteNumber
  }
 }

==0x2d8==
 struct PACKET_CZ_CONFIG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long Config
  /* this+0x6 */ int Value
 }

==0x2d9==
 struct PACKET_ZC_CONFIG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long Config
  /* this+0x6 */ int Value
 }

==0x2da==
 struct PACKET_ZC_CONFIG_NOTIFY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool bOpenEquipmentWin
 }

==0x2db==
 struct PACKET_CZ_BATTLEFIELD_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ char msg[...]
 }

==0x2dc==
 struct PACKET_ZC_BATTLEFIELD_CHAT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long accountID
  /* this+0x8 */ char name[24]
  /* this+0x20 */ char msg[...]
 }

==0x2dd==
 struct PACKET_ZC_BATTLEFIELD_NOTIFY_CAMPINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long accountID
  /* this+0x6 */ char name[24]
  /* this+0x1e */ short camp
 }

==0x2de==
 struct PACKET_ZC_BATTLEFIELD_NOTIFY_POINT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short pointCampA
  /* this+0x4 */ short pointCampB
 }

==0x2df==
 struct PACKET_ZC_BATTLEFIELD_NOTIFY_POSITION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long accountID
  /* this+0x6 */ char name[24]
  /* this+0x1e */ unsigned short job
  /* this+0x20 */ short x
  /* this+0x22 */ short y
 }

==0x2e0==
 struct PACKET_ZC_BATTLEFIELD_NOTIFY_HP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long accountID
  /* this+0x6 */ char name[24]
  /* this+0x1e */ short hp
  /* this+0x20 */ short maxHp
 }

==0x2e1==
 struct PACKET_ZC_NOTIFY_ACT2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned long targetGID
  /* this+0xa */ unsigned long startTime
  /* this+0xe */ int attackMT
  /* this+0x12 */ int attackedMT
  /* this+0x16 */ int damage
  /* this+0x1a */ short count
  /* this+0x1c */ unsigned char action
  /* this+0x1d */ int leftDamage
 }

==0x2e6==
 struct PACKET_CZ_BOT_CHECK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int IsBot
 }

==0x2e7==
 struct PACKET_ZC_MAPPROPERTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short type
  /* this+0x6 */ int mapInfoTable[...]
 }

==0x2e8==
 struct PACKET_ZC_NORMAL_ITEMLIST3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO3 ItemInfo[...] { // Size 22
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x12 */ long HireExpireDate
  }
 }

==0x2e9==
 struct PACKET_ZC_CART_NORMAL_ITEMLIST3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO3 ItemInfo[...] { // Size 22
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x12 */ long HireExpireDate
  }
 }

==0x2ea==
 struct PACKET_ZC_STORE_NORMAL_ITEMLIST3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct NORMALITEM_EXTRAINFO3 ItemInfo[...] { // Size 22
    /* this+0x0 */ short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ unsigned char type
    /* this+0x5 */ bool IsIdentified
    /* this+0x6 */ short count
    /* this+0x8 */ unsigned short WearState
    /* this+0xa */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
    /* this+0x12 */ long HireExpireDate
  }
 }

==0x2eb==
 struct PACKET_ZC_ACCEPT_ENTER2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long startTime
  /* this+0x6 */ unsigned char PosDir[3]
  /* this+0x9 */ unsigned char xSize
  /* this+0xa */ unsigned char ySize
  /* this+0xb */ short font
 }

==0x2ec==
 struct PACKET_ZC_NOTIFY_MOVEENTRY4 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char objecttype
  /* this+0x3 */ unsigned long GID
  /* this+0x7 */ short speed
  /* this+0x9 */ short bodyState
  /* this+0xb */ short healthState
  /* this+0xd */ int effectState
  /* this+0x11 */ short job
  /* this+0x13 */ short head
  /* this+0x15 */ int weapon
  /* this+0x19 */ short accessory
  /* this+0x1b */ unsigned long moveStartTime
  /* this+0x1f */ short accessory2
  /* this+0x21 */ short accessory3
  /* this+0x23 */ short headpalette
  /* this+0x25 */ short bodypalette
  /* this+0x27 */ short headDir
  /* this+0x29 */ unsigned long GUID
  /* this+0x2d */ short GEmblemVer
  /* this+0x2f */ short honor
  /* this+0x31 */ int virtue
  /* this+0x35 */ bool isPKModeON
  /* this+0x36 */ unsigned char sex
  /* this+0x37 */ unsigned char MoveData[6]
  /* this+0x3d */ unsigned char xSize
  /* this+0x3e */ unsigned char ySize
  /* this+0x3f */ short clevel
  /* this+0x41 */ short font
 }

==0x2ed==
 struct PACKET_ZC_NOTIFY_NEWENTRY4 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ int effectState
  /* this+0x10 */ short job
  /* this+0x12 */ short head
  /* this+0x14 */ int weapon
  /* this+0x18 */ short accessory
  /* this+0x1a */ short accessory2
  /* this+0x1c */ short accessory3
  /* this+0x1e */ short headpalette
  /* this+0x20 */ short bodypalette
  /* this+0x22 */ short headDir
  /* this+0x24 */ unsigned long GUID
  /* this+0x28 */ short GEmblemVer
  /* this+0x2a */ short honor
  /* this+0x2c */ int virtue
  /* this+0x30 */ bool isPKModeON
  /* this+0x31 */ unsigned char sex
  /* this+0x32 */ unsigned char PosDir[3]
  /* this+0x35 */ unsigned char xSize
  /* this+0x36 */ unsigned char ySize
  /* this+0x37 */ short clevel
  /* this+0x39 */ short font
 }

==0x2ee==
 struct PACKET_ZC_NOTIFY_STANDENTRY4 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ short speed
  /* this+0x8 */ short bodyState
  /* this+0xa */ short healthState
  /* this+0xc */ int effectState
  /* this+0x10 */ short job
  /* this+0x12 */ short head
  /* this+0x14 */ int weapon
  /* this+0x18 */ short accessory
  /* this+0x1a */ short accessory2
  /* this+0x1c */ short accessory3
  /* this+0x1e */ short headpalette
  /* this+0x20 */ short bodypalette
  /* this+0x22 */ short headDir
  /* this+0x24 */ unsigned long GUID
  /* this+0x28 */ short GEmblemVer
  /* this+0x2a */ short honor
  /* this+0x2c */ int virtue
  /* this+0x30 */ bool isPKModeON
  /* this+0x31 */ unsigned char sex
  /* this+0x32 */ unsigned char PosDir[3]
  /* this+0x35 */ unsigned char xSize
  /* this+0x36 */ unsigned char ySize
  /* this+0x37 */ unsigned char state
  /* this+0x38 */ short clevel
  /* this+0x3a */ short font
 }

==0x2ef==
 struct PACKET_ZC_NOTIFY_FONT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short font
 }

==0x2f0==
 struct PACKET_ZC_PROGRESS {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long color
  /* this+0x6 */ unsigned long time
 }

==0x2f1==
 struct PACKET_CZ_PROGRESS {
  /* this+0x0 */ short PacketType
 }

==0x2f2==
 struct PACKET_ZC_PROGRESS_CANCEL {
  /* this+0x0 */ short PacketType
 }

==0x35c==
 struct PACKET_CZ_OPEN_SIMPLE_CASHSHOP_ITEMLIST {
  /* this+0x0 */ short PacketType
 }

==0x35d==
 struct PACKET_ZC_SIMPLE_CASHSHOP_POINT_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long CashPoint
  /* this+0x8 */ short md_itemcount
  /* this+0xa */ short md_itemSize
  /* this+0xc */ short best_itemcount
  /* this+0xe */ short best_itemsize
  /* this+0x10 */ struct PURCHASE_ITEM ItemList[...] { // Size 11
    /* this+0x0 */ int price
    /* this+0x4 */ int discountprice
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
  }
 }

==0x35e==
 struct PACKET_CZ_CLOSE_WINDOW {
  /* this+0x0 */ short PacketType
 }

==0x3dd==
 struct PACKET_AHC_GAME_GUARD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuthData[4]
 }

==0x3de==
 struct PACKET_CAH_ACK_GAME_GUARD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AuthData[4]
 }

==0x436==
 struct PACKET_CZ_ENTER2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long GID
  /* this+0xa */ int AuthCode
  /* this+0xe */ unsigned long clientTime
  /* this+0x12 */ unsigned char Sex
 }

==0x437==
 struct PACKET_CZ_REQUEST_ACT2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long targetGID
  /* this+0x6 */ unsigned char action
 }

==0x438==
 struct PACKET_CZ_USE_SKILL2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short selectedLevel
  /* this+0x4 */ unsigned short SKID
  /* this+0x6 */ unsigned long targetID
 }

==0x439==
 struct PACKET_CZ_USE_ITEM2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short index
  /* this+0x4 */ unsigned long AID
 }

==0x43d==
 struct PACKET_ZC_SKILL_POSTDELAY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ unsigned long DelayTM
 }

==0x43e==
 struct PACKET_ZC_SKILL_POSTDELAY_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct SKILL_POSTDELAY delayList[...] { // Size 6
    /* this+0x0 */ unsigned short SKID
    /* this+0x2 */ unsigned long DelayTM
  }
 }

==0x43f==
 struct PACKET_ZC_MSG_STATE_CHANGE2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ bool state
  /* this+0x9 */ unsigned long RemainMS
  /* this+0xd */ int val[3]
 }

==0x440==
 struct PACKET_ZC_MILLENNIUMSHIELD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ short num
  /* this+0x8 */ short state
 }

==0x441==
 struct PACKET_ZC_SKILLINFO_DELETE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
 }

==0x442==
 struct PACKET_ZC_SKILL_SELECT_REQUEST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ long why
  /* this+0x8 */ unsigned short SKIDList[...]
 }

==0x443==
 struct PACKET_CZ_SKILL_SELECT_RESPONSE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long why
  /* this+0x6 */ unsigned short SKID
 }

==0x444==
 struct PACKET_ZC_SIMPLE_CASH_POINT_ITEMLIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long CashPoint
  /* this+0x8 */ struct PURCHASE_ITEM ItemList[...] { // Size 11
    /* this+0x0 */ int price
    /* this+0x4 */ int discountprice
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
  }
 }

==0x445==
 struct PACKET_CZ_SIMPLE_BUY_CASH_POINT_ITEM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ITID
  /* this+0x4 */ short count
 }

==0x446==
 struct PACKET_ZC_QUEST_NOTIFY_EFFECT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long npcID
  /* this+0x6 */ short xPos
  /* this+0x8 */ short yPos
  /* this+0xa */ short effect
  /* this+0xc */ short type
 }

==0x447==
 struct PACKET_CZ_BLOCKING_PLAY_CANCEL {
  /* this+0x0 */ short PacketType
 }

==0x448==
 struct PACKET_HC_CHARACTER_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ struct CHARACTER_LIST CharacterList[...] { // Size 5
    /* this+0x0 */ unsigned long dwGID
    /* this+0x4 */ unsigned char SlotIdx
  }
 }

==0x449==
 struct PACKET_ZC_HACKSH_ERROR_MSG {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short ErrorID
 }

==0x44a==
 struct PACKET_CZ_CLIENT_VERSION {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long clientVer
 }

==0x44b==
 struct PACKET_CZ_CLOSE_SIMPLECASH_SHOP {
  /* this+0x0 */ short PacketType
 }

==0x7d0==
 struct PACKET_ZC_ES_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short esNo
  /* this+0x4 */ short esMsg
 }

==0x7d1==
 struct PACKET_CZ_ES_GET_LIST {
  /* this+0x0 */ short PacketType
 }

==0x7d2==
 struct PACKET_ZC_ES_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short Count
 }

==0x7d3==
 struct PACKET_CZ_ES_CHOOSE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short esNo
 }

==0x7d4==
 struct PACKET_CZ_ES_CANCEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short esNo
 }

==0x7d5==
 struct PACKET_ZC_ES_READY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short esNo
 }

==0x7d6==
 struct PACKET_ZC_ES_GOTO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short esNo
 }

==0x7d7==
 struct PACKET_CZ_GROUPINFO_CHANGE_V2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long expOption
  /* this+0x6 */ unsigned char ItemPickupRule
  /* this+0x7 */ unsigned char ItemDivisionRule
 }

==0x7d8==
 struct PACKET_ZC_REQ_GROUPINFO_CHANGE_V2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long expOption
  /* this+0x6 */ unsigned char ItemPickupRule
  /* this+0x7 */ unsigned char ItemDivisionRule
 }

==0x7d9==
 struct PACKET_ZC_SHORTCUT_KEY_LIST_V2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct ShortCutKey ShortCutKey[38] { // Size 7
    /* this+0x0 */ char isSkill
    /* this+0x1 */ unsigned long ID
    /* this+0x5 */ short count
  }
 }

==0x7da==
 struct PACKET_CZ_CHANGE_GROUP_MASTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
 }

==0x7db==
 struct PACKET_ZC_HO_PAR_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short var
  /* this+0x4 */ int value
 }

==0x7dc==
 struct PACKET_CZ_SEEK_PARTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Option
 }

==0x7dd==
 struct PACKET_ZC_SEEK_PARTY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Name[24]
  /* this+0x1a */ unsigned long Job
  /* this+0x1e */ unsigned long Level
  /* this+0x22 */ char mapName[16]
  /* this+0x32 */ unsigned long Option
 }

==0x7de==
 struct PACKET_CZ_SEEK_PARTY_MEMBER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Job
  /* this+0x6 */ unsigned long Level
  /* this+0xa */ char mapName[16]
  /* this+0x1a */ unsigned long Option
 }

==0x7df==
 struct PACKET_ZC_SEEK_PARTY_MEMBER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Name[24]
  /* this+0x1a */ unsigned long Job
  /* this+0x1e */ unsigned long Level
  /* this+0x22 */ char mapName[16]
  /* this+0x32 */ unsigned long Option
 }

==0x7e0==
 struct PACKET_ZC_ES_NOTI_MYINFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short esNo
  /* this+0x4 */ char esname[54]
 }

==0x7e1==
 struct PACKET_ZC_SKILLINFO_UPDATE2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ int type
  /* this+0x8 */ short level
  /* this+0xa */ short spcost
  /* this+0xc */ short attackRange
  /* this+0xe */ bool upgradable
 }

==0x7e2==
 struct PACKET_ZC_MSG_VALUE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short msg
  /* this+0x4 */ int value
 }

==0x7e3==
 struct PACKET_ZC_ITEMLISTWIN_OPEN {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ long Type
 }

==0x7e4==
 struct PACKET_CZ_ITEMLISTWIN_RES {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ long Type
  /* this+0x8 */ long Action
  /* this+0xc */ unsigned short MaterialList
 }

==0x7e5==
 struct PACKET_CH_ENTER_CHECKBOT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long dwAID
  /* this+0x8 */ char szStringInfo[...]
 }

==0x7e6==
 struct PACKET_ZC_MSG_SKILL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short SKID
  /* this+0x4 */ int MSGID
 }

==0x7e7==
 struct PACKET_CH_CHECKBOT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long dwAID
  /* this+0x8 */ char szStringInfo[24]
 }

==0x7e8==
 struct PACKET_HC_CHECKBOT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char img[...]
 }

==0x7e9==
 struct PACKET_HC_CHECKBOT_RESULT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char Result
 }

==0x7ea==
 struct PACKET_CZ_BATTLE_FIELD_LIST {
  /* this+0x0 */ short PacketType
 }

==0x7eb==
 struct PACKET_ZC_BATTLE_FIELD_LIST {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ short Count
  /* this+0x6 */ short ack_type
  /* this+0x8 */ struct BATTLE_FIELD_INFO InfoList[...] { // Size 62
    /* this+0x0 */ unsigned long BFNO
    /* this+0x4 */ char BattleFieldName[56]
    /* this+0x3c */ short JoinTeam
  }
 }

==0x7ec==
 struct PACKET_CZ_JOIN_BATTLE_FIELD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
  /* this+0x6 */ short JoinTeam
 }

==0x7ed==
 struct PACKET_ZC_JOIN_BATTLE_FIELD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
  /* this+0x6 */ short JoinTeam
  /* this+0x8 */ short Result
 }

==0x7ee==
 struct PACKET_CZ_CANCEL_BATTLE_FIELD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
 }

==0x7ef==
 struct PACKET_ZC_CANCEL_BATTLE_FIELD {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
  /* this+0x6 */ short Result
 }

==0x7f0==
 struct PACKET_CZ_REQ_BATTLE_STATE_MONITOR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
  /* this+0x6 */ short PowerSwitch
 }

==0x7f1==
 struct PACKET_ZC_ACK_BATTLE_STATE_MONITOR {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
  /* this+0x6 */ short PlayCount
  /* this+0x8 */ short BattleState
  /* this+0xa */ short TeamCount_A
  /* this+0xc */ short TeamCount_B
  /* this+0xe */ short MyCount
  /* this+0x10 */ short JoinTeam
 }

==0x7f2==
 struct PACKET_ZC_BATTLE_NOTI_START_STEP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
  /* this+0x6 */ short Result
 }

==0x7f3==
 struct PACKET_ZC_BATTLE_JOIN_NOTI_DEFER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long BFNO
 }

==0x7f4==
 struct PACKET_ZC_BATTLE_JOIN_DISABLE_STATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool Enable
 }

==0x7f5==
 struct PACKET_CZ_GM_FULLSTRIP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long TargetAID
 }

==0x7f6==
 struct PACKET_ZC_NOTIFY_EXP {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int amount
  /* this+0xa */ unsigned short varID
  /* this+0xc */ short expType
 }

==0x7f7==
 struct PACKET_ZC_NOTIFY_MOVEENTRY7 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char objecttype
  /* this+0x5 */ unsigned long GID
  /* this+0x9 */ short speed
  /* this+0xb */ short bodyState
  /* this+0xd */ short healthState
  /* this+0xf */ int effectState
  /* this+0x13 */ short job
  /* this+0x15 */ short head
  /* this+0x17 */ int weapon
  /* this+0x1b */ short accessory
  /* this+0x1d */ unsigned long moveStartTime
  /* this+0x21 */ short accessory2
  /* this+0x23 */ short accessory3
  /* this+0x25 */ short headpalette
  /* this+0x27 */ short bodypalette
  /* this+0x29 */ short headDir
  /* this+0x2b */ unsigned long GUID
  /* this+0x2f */ short GEmblemVer
  /* this+0x31 */ short honor
  /* this+0x33 */ int virtue
  /* this+0x37 */ bool isPKModeON
  /* this+0x38 */ unsigned char sex
  /* this+0x39 */ unsigned char MoveData[6]
  /* this+0x3f */ unsigned char xSize
  /* this+0x40 */ unsigned char ySize
  /* this+0x41 */ short clevel
  /* this+0x43 */ short font
  /* this+0x45 */ unsigned char name[24]
 }

==0x7f8==
 struct PACKET_ZC_NOTIFY_NEWENTRY5 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char objecttype
  /* this+0x5 */ unsigned long GID
  /* this+0x9 */ short speed
  /* this+0xb */ short bodyState
  /* this+0xd */ short healthState
  /* this+0xf */ int effectState
  /* this+0x13 */ short job
  /* this+0x15 */ short head
  /* this+0x17 */ int weapon
  /* this+0x1b */ short accessory
  /* this+0x1d */ short accessory2
  /* this+0x1f */ short accessory3
  /* this+0x21 */ short headpalette
  /* this+0x23 */ short bodypalette
  /* this+0x25 */ short headDir
  /* this+0x27 */ unsigned long GUID
  /* this+0x2b */ short GEmblemVer
  /* this+0x2d */ short honor
  /* this+0x2f */ int virtue
  /* this+0x33 */ bool isPKModeON
  /* this+0x34 */ unsigned char sex
  /* this+0x35 */ unsigned char PosDir[3]
  /* this+0x38 */ unsigned char xSize
  /* this+0x39 */ unsigned char ySize
  /* this+0x3a */ short clevel
  /* this+0x3c */ short font
  /* this+0x3e */ unsigned char name[24]
 }

==0x7f9==
 struct PACKET_ZC_NOTIFY_STANDENTRY5 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char objecttype
  /* this+0x5 */ unsigned long GID
  /* this+0x9 */ short speed
  /* this+0xb */ short bodyState
  /* this+0xd */ short healthState
  /* this+0xf */ int effectState
  /* this+0x13 */ short job
  /* this+0x15 */ short head
  /* this+0x17 */ int weapon
  /* this+0x1b */ short accessory
  /* this+0x1d */ short accessory2
  /* this+0x1f */ short accessory3
  /* this+0x21 */ short headpalette
  /* this+0x23 */ short bodypalette
  /* this+0x25 */ short headDir
  /* this+0x27 */ unsigned long GUID
  /* this+0x2b */ short GEmblemVer
  /* this+0x2d */ short honor
  /* this+0x2f */ int virtue
  /* this+0x33 */ bool isPKModeON
  /* this+0x34 */ unsigned char sex
  /* this+0x35 */ unsigned char PosDir[3]
  /* this+0x38 */ unsigned char xSize
  /* this+0x39 */ unsigned char ySize
  /* this+0x3a */ unsigned char state
  /* this+0x3b */ short clevel
  /* this+0x3d */ short font
  /* this+0x3f */ unsigned char name[24]
 }

==0x7fa==
 struct PACKET_ZC_DELETE_ITEM_FROM_BODY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short DeleteType
  /* this+0x4 */ unsigned short Index
  /* this+0x6 */ short Count
 }

==0x7fb==
 struct PACKET_ZC_USESKILL_ACK2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long targetID
  /* this+0xa */ short xPos
  /* this+0xc */ short yPos
  /* this+0xe */ unsigned short SKID
  /* this+0x10 */ unsigned long property
  /* this+0x14 */ unsigned long delayTime
  /* this+0x18 */ bool isDisposable
 }

==0x7fc==
 struct PACKET_ZC_CHANGE_GROUP_MASTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long OldMasterAID
  /* this+0x6 */ unsigned long NewMasterAID
 }

==0x7fe==
 struct PACKET_ZC_PLAY_NPC_BGM {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char Bgm[24]
 }

==0x7ff==
 struct PACKET_ZC_DEFINE_CHECK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ int Result
 }

==0x800==
 struct PACKET_ZC_PC_PURCHASE_ITEMLIST_FROMMC2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long UniqueID
  /* this+0xc */ struct PURCHASE_ITEM_FROMMC itemList[...] { // Size 22
    /* this+0x0 */ int price
    /* this+0x4 */ short count
    /* this+0x6 */ short index
    /* this+0x8 */ unsigned char type
    /* this+0x9 */ unsigned short ITID
    /* this+0xb */ unsigned char IsIdentified
    /* this+0xc */ unsigned char IsDamaged
    /* this+0xd */ unsigned char refiningLevel
    /* this+0xe */ struct EQUIPSLOTINFO slot {
      /* this+0x0 */ unsigned short card1
      /* this+0x2 */ unsigned short card2
      /* this+0x4 */ unsigned short card3
      /* this+0x6 */ unsigned short card4
    }
  }
 }

==0x801==
 struct PACKET_CZ_PC_PURCHASE_ITEMLIST_FROMMC2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ unsigned long UniqueID
  /* this+0xc */ struct CZ_PURCHASE_ITEM_FROMMC itemList[...] { // Size 4
    /* this+0x0 */ short count
    /* this+0x2 */ short index
  }
 }

==0x802==
 struct PACKET_CZ_PARTY_BOOKING_REQ_REGISTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct PARTY_BOOKING_DETAIL RegisterInfo {
    /* this+0x0 */ short Level
    /* this+0x2 */ short MapID
    /* this+0x4 */ short Job[6]
  }
 }

==0x803==
 struct PACKET_ZC_PARTY_BOOKING_ACK_REGISTER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
 }

==0x804==
 struct PACKET_CZ_PARTY_BOOKING_REQ_SEARCH {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Level
  /* this+0x4 */ short MapID
  /* this+0x6 */ short Job
  /* this+0x8 */ unsigned long LastIndex
  /* this+0xc */ short ResultCount
 }

==0x805==
 struct PACKET_ZC_PARTY_BOOKING_ACK_SEARCH {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ bool IsExistMoreResult
  /* this+0x5 */ struct PARTY_BOOKING_AD_INFO Info[...] { // Size 48
    /* this+0x0 */ unsigned long Index
    /* this+0x4 */ char CharName[24]
    /* this+0x1c */ long ExpireTime
    /* this+0x20 */ struct PARTY_BOOKING_DETAIL Detail {
      /* this+0x0 */ short Level
      /* this+0x2 */ short MapID
      /* this+0x4 */ short Job[6]
    }
  }
 }

==0x806==
 struct PACKET_CZ_PARTY_BOOKING_REQ_DELETE {
  /* this+0x0 */ short PacketType
 }

==0x807==
 struct PACKET_ZC_PARTY_BOOKING_ACK_DELETE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
 }

==0x808==
 struct PACKET_CZ_PARTY_BOOKING_REQ_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Job[6]
 }

==0x809==
 struct PACKET_ZC_PARTY_BOOKING_NOTIFY_INSERT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ struct PARTY_BOOKING_AD_INFO Info {
    /* this+0x0 */ unsigned long Index
    /* this+0x4 */ char CharName[24]
    /* this+0x1c */ long ExpireTime
    /* this+0x20 */ struct PARTY_BOOKING_DETAIL Detail {
      /* this+0x0 */ short Level
      /* this+0x2 */ short MapID
      /* this+0x4 */ short Job1
      /* this+0x6 */ short Job2
      /* this+0x8 */ short Job3
      /* this+0xa */ short Job4
      /* this+0xc */ short Job5
      /* this+0xe */ short Job6
    }
  }
 }

==0x80a==
 struct PACKET_ZC_PARTY_BOOKING_NOTIFY_UPDATE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Index
  /* this+0x6 */ short Job1
  /* this+0x8 */ short Job2
  /* this+0xa */ short Job3
  /* this+0xc */ short Job4
  /* this+0xe */ short Job5
  /* this+0x10 */ short Job6
 }

==0x80b==
 struct PACKET_ZC_PARTY_BOOKING_NOTIFY_DELETE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long Index
 }

==0x80c==
 struct PACKET_CZ_SIMPLE_CASH_BTNSHOW {
  /* this+0x0 */ short PacketType
 }

==0x80d==
 struct PACKET_ZC_SIMPLE_CASH_BTNSHOW {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ bool show
 }

==0x80e==
 struct PACKET_ZC_NOTIFY_HP_TO_GROUPM_R2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ int hp
  /* this+0xa */ int maxhp
 }

==0x80f==
 struct PACKET_ZC_ADD_EXCHANGE_ITEM2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ITID
  /* this+0x4 */ unsigned char type
  /* this+0x5 */ int count
  /* this+0x9 */ bool IsIdentified
  /* this+0xa */ bool IsDamaged
  /* this+0xb */ unsigned char refiningLevel
  /* this+0xc */ struct EQUIPSLOTINFO slot {
    /* this+0x0 */ unsigned short card1
    /* this+0x2 */ unsigned short card2
    /* this+0x4 */ unsigned short card3
    /* this+0x6 */ unsigned short card4
  }
 }

==0x810==
 struct PACKET_ZC_OPEN_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char count
 }

==0x811==
 struct PACKET_CZ_REQ_OPEN_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long LimitZeny
  /* this+0x8 */ unsigned char result
  /* this+0x9 */ char storeName[80]
  /* this+0x59 */ struct PRODUCTINFO_IN_BUYING_STORE ItemList[...] { // Size 8
    /* this+0x0 */ unsigned short ITID
    /* this+0x2 */ short count
    /* this+0x4 */ int price
  }
 }

==0x812==
 struct PACKET_ZC_FAILED_OPEN_BUYING_STORE_TO_BUYER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ int total_weight
 }

==0x813==
 struct PACKET_ZC_MYITEMLIST_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long AID
  /* this+0x8 */ int limitZeny
  /* this+0xc */ struct BUYING_STORE_ITEMLIST ItemList[...] { // Size 9
    /* this+0x0 */ int price
    /* this+0x4 */ short count
    /* this+0x6 */ unsigned char type
    /* this+0x7 */ unsigned short ITID
  }
 }

==0x814==
 struct PACKET_ZC_BUYING_STORE_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long makerAID
  /* this+0x6 */ char storeName[80]
 }

==0x815==
 struct PACKET_CZ_REQ_CLOSE_BUYING_STORE {
  /* this+0x0 */ short PacketType
 }

==0x816==
 struct PACKET_ZC_DISAPPEAR_BUYING_STORE_ENTRY {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long makerAID
 }

==0x817==
 struct PACKET_CZ_REQ_CLICK_TO_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long makerAID
 }

==0x818==
 struct PACKET_ZC_ACK_ITEMLIST_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long makerAID
  /* this+0x8 */ unsigned long StoreID
  /* this+0xc */ int limitZeny
  /* this+0x10 */ struct BUYING_STORE_ITEMLIST ItemList[...] { // Size 9
    /* this+0x0 */ int price
    /* this+0x4 */ short count
    /* this+0x6 */ unsigned char type
    /* this+0x7 */ unsigned short ITID
  }
 }

==0x819==
 struct PACKET_CZ_REQ_TRADE_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long makerAID
  /* this+0x8 */ unsigned long StoreID
  /* this+0xc */ struct TRADE_ITEM_BUYING_STORE ItemList[...] { // Size 6
    /* this+0x0 */ unsigned short index
    /* this+0x2 */ unsigned short ITID
    /* this+0x4 */ short count
  }
 }

==0x81a==
 struct PACKET_ZC_FAILED_TRADE_BUYING_STORE_TO_BUYER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
 }

==0x81b==
 struct PACKET_ZC_UPDATE_ITEM_FROM_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short ITID
  /* this+0x4 */ short count
  /* this+0x6 */ int limitZeny
 }

==0x81c==
 struct PACKET_ZC_ITEM_DELETE_BUYING_STORE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short index
  /* this+0x4 */ short count
  /* this+0x6 */ int zeny
 }

==0x81d==
 struct PACKET_ZC_EL_INIT {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ int AID
  /* this+0x6 */ int hp
  /* this+0xa */ int maxHP
  /* this+0xe */ int sp
  /* this+0x12 */ int maxSP
 }

==0x81e==
 struct PACKET_ZC_EL_PAR_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short var
  /* this+0x4 */ int value
 }

==0x81f==
 struct PACKET_ZC_BROADCAST4 {
  /* this+0x0 */ short PakcetType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char Msgtype
  /* this+0x5 */ unsigned long ColorRGB
  /* this+0x9 */ char msg[...]
 }

==0x820==
 struct PACKET_ZC_COSTUME_SPRITE_CHANGE {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ unsigned char type
  /* this+0x7 */ int value
 }

==0x821==
 struct PACKET_AC_OTP_USER {
  /* this+0x0 */ short PacketType
 }

==0x822==
 struct PACKET_CA_OTP_AUTH_REQ {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char OTPCode[7]
 }

==0x823==
 struct PACKET_AC_OTP_AUTH_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned short LoginResult
 }

==0x824==
 struct PACKET_ZC_FAILED_TRADE_BUYING_STORE_TO_SELLER {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short Result
  /* this+0x4 */ unsigned short ITID
 }

==0x825a==
 struct PACKET_CA_SSO_LOGIN_REQa {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long Version
  /* this+0x8 */ unsigned char clienttype
  /* this+0x9 */ char ID[24]
  /* this+0x21 */ char MacAddr[17]
  /* this+0x32 */ char IpAddr[15]
  /* this+0x41 */ char t1[...]
 }

==0x825==
 struct PACKET_CA_SSO_LOGIN_REQ {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned long Version
  /* this+0x8 */ unsigned char clienttype
  /* this+0x9 */ unsigned char ID[24]
  /* this+0x21 */ unsigned char Passwd[27]
  /* this+0x3c */ char MacAdress[17]
  /* this+0x4d */ char IP[15]
  /* this+0x5c */ char t1[...]
 }

==0x826==
 struct PACKET_AC_SSO_LOGIN_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned short Result
 }

==0x827==
 struct PACKET_CH_DELETE_CHAR3_RESERVED {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
 }

==0x828==
 struct PACKET_HC_DELETE_CHAR3_RESERVED {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ int Result
  /* this+0xa */ long DeleteReservedDate
 }

==0x829==
 struct PACKET_CH_DELETE_CHAR3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ char Birth[6]
 }

==0x82a==
 struct PACKET_HC_DELETE_CHAR3 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ int Result
 }

==0x82b==
 struct PACKET_CH_DELETE_CHAR3_CANCEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
 }

==0x82c==
 struct PACKET_HC_DELETE_CHAR3_CANCEL {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long GID
  /* this+0x6 */ int Result
 }

==0x835==
 struct PACKET_CZ_SEARCH_STORE_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ unsigned char StoreType
  /* this+0x5 */ unsigned long maxPrice
  /* this+0x9 */ unsigned long minPrice
  /* this+0xd */ unsigned char ItemIDListSize
  /* this+0xe */ unsigned char CardIDListSize
 }

==0x836==
 struct PACKET_ZC_SEARCH_STORE_INFO_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short PacketLength
  /* this+0x4 */ bool IsFirstPage
  /* this+0x5 */ bool IsNexPage
  /* this+0x6 */ unsigned char RemainedSearchCnt
  /* this+0x7 */ struct ResultItemInfo SSI_List[...] { // Size 106
    /* this+0x0 */ unsigned int SSI_ID
    /* this+0x4 */ unsigned int AID
    /* this+0x8 */ char StoreName[80]
    /* this+0x58 */ unsigned short ITID
    /* this+0x5a */ unsigned char ItemType
    /* this+0x5b */ int price
    /* this+0x5f */ unsigned short count
    /* this+0x61 */ unsigned char refiningLevel
    /* this+0x62 */ unsigned short card1
    /* this+0x64 */ unsigned short card2
    /* this+0x66 */ unsigned short card3
    /* this+0x68 */ unsigned short card4
  }
 }

==0x837==
 struct PACKET_ZC_SEARCH_STORE_INFO_FAILED {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char Reason
 }

==0x838==
 struct PACKET_CZ_SEARCH_STORE_INFO_NEXT_PAGE {
  /* this+0x0 */ short PacketType
 }

==0x839==
 struct PACKET_ZC_ACK_BAN_GUILD_SSO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ char charName[24]
  /* this+0x1a */ char reasonDesc[40]
 }

==0x83a==
 struct PACKET_ZC_OPEN_SEARCH_STORE_INFO {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short OpenType
  /* this+0x4 */ unsigned char SearchCntMax
 }

==0x83b==
 struct PACKET_CZ_CLOSE_SEARCH_STORE_INFO {
  /* this+0x0 */ short PacketType
 }

==0x83c==
 struct PACKET_CZ_SSILIST_ITEM_CLICK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned long AID
  /* this+0x6 */ unsigned long SSI_ID
  /* this+0xa */ unsigned short ITID
 }

==0x83d==
 struct PACKET_ZC_SSILIST_ITEM_CLICK_ACK {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ short x
  /* this+0x4 */ short y
 }

==0x83e==
 struct PACKET_AC_REFUSE_LOGIN_R2 {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned int ErrorCode
  /* this+0x6 */ char blockDate[20]
 }

==0x841==
 struct PACKET_CH_SELECT_ACCESSIBLE_MAPNAME {
  /* this+0x0 */ short PacketType
  /* this+0x2 */ unsigned char CharNum
  /* this+0x3 */ unsigned char mapListNum
 }
[[Category:Incomplete]][[Category:Database]][[Category:Source Snippets]]