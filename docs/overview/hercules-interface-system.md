!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.


The **Interfaces** are the core of the **[Hercules Plugin Manager](../customization/hercules-plugin-manager.md)**, providinga
higher amount of flexibility when working with source code modifications through
[Functions Overloading](../customization/hercules-plugin-manager.md#hpm-function-overloading)

# Current Interface Functions

- Common
  - console
  - DB
  - SQL
  - strlib
  - sv
  - StrBuf (StringBuf)
  - iTimer
- Map Server
  - atcommand
  - battle
  - buyingstore
  - clif
  - guild
  - homunculus
  - ircbot
  - log
  - iMap
  - party
  - pc
  - script
  - searchstore
  - skill
  - vending
- Char Server
  - pincode

# Interface Referencing Functions

You can find a list of Interface functions, to which function they point and what where they known as in other emulators
or in the past if the current function name differs from the old one.

## Common

### Console

[Back to Table of Contents](#toc "wikilink")

| Interface Name            | Function Name             |
|---------------------------|---------------------------|
| console->init            | console_init               |
| console->init            | console_init               |
| console->final           | console_final              |
| console->display_title   | display_title              |
| console->parse_init      | console_parse_init         |
| console->parse_final     | console_parse_final        |
| console->parse_timer     | console_parse_timer        |
| console->pthread_main    | cThread_main               |
| console->parse           | console_parse              |
| console->parse_sub       | console_parse_sub          |
| console->key_pressed     | console_parse_key_pressed  |
| console->load_defaults   | console_load_defaults      |
| console->parse_list_subs | console_parse_list_subs    |
| console->addCommand      | console_parse_create       |

### DB

[Back to Table of Contents](#toc "wikilink")

| Interface Name       | Function Name      |
|----------------------|--------------------|
| DB->alloc           | db_alloc            |
| DB->custom_release  | db_custom_release   |
| DB->data2i          | db_data2i           |
| DB->data2ptr        | db_data2ptr         |
| DB->data2ui         | db_data2ui          |
| DB->default_cmp     | db_default_cmp      |
| DB->default_hash    | db_default_hash     |
| DB->default_release | db_default_release  |
| DB->final           | db_final            |
| DB->fix_options     | db_fix_options      |
| DB->i2data          | db_i2data           |
| DB->i2key           | db_i2key            |
| DB->init            | db_init             |
| DB->ptr2data        | db_ptr2data         |
| DB->str2key         | db_str2key          |
| DB->ui2data         | db_ui2data          |
| DB->ui2key          | db_ui2key           |

### SQL

[Back to Table of Contents](#toc "wikilink")

| Interface Name         | Function Name        |
|------------------------|----------------------|
| SQL->Connect          | Sql_Connect           |
| SQL->GetTimeout       | Sql_GetTimeout        |
| SQL->GetColumnNames   | Sql_GetColumnNames    |
| SQL->SetEncoding      | Sql_SetEncoding       |
| SQL->Ping             | Sql_Ping              |
| SQL->EscapeString     | Sql_EscapeString      |
| SQL->EscapeStringLen  | Sql_EscapeStringLen   |
| SQL->Query            | Sql_Query             |
| SQL->QueryV           | Sql_QueryV            |
| SQL->QueryStr         | Sql_QueryStr          |
| SQL->LastInsertId     | Sql_LastInsertId      |
| SQL->NumColumns       | Sql_NumColumns        |
| SQL->NumRows          | Sql_NumRows           |
| SQL->NextRow          | Sql_NextRow           |
| SQL->GetData          | Sql_GetData           |
| SQL->FreeResult       | Sql_FreeResult        |
| SQL->ShowDebug\_      | Sql_ShowDebug\_       |
| SQL->Free             | Sql_Free              |
| SQL->Malloc           | Sql_Malloc            |
| SQL->StmtBindColumn   | SqlStmt_BindColumn    |
| SQL->StmtBindParam    | SqlStmt_BindParam     |
| SQL->StmtExecute      | SqlStmt_Execute       |
| SQL->StmtFree         | SqlStmt_Free          |
| SQL->StmtFreeResult   | SqlStmt_FreeResult    |
| SQL->StmtLastInsertId | SqlStmt_LastInsertId  |
| SQL->StmtMalloc       | SqlStmt_Malloc        |
| SQL->StmtNextRow      | SqlStmt_NextRow       |
| SQL->StmtNumColumns   | SqlStmt_NumColumns    |
| SQL->StmtNumParams    | SqlStmt_NumParams     |
| SQL->StmtNumRows      | SqlStmt_NumRows       |
| SQL->StmtPrepare      | SqlStmt_Prepare       |
| SQL->StmtPrepareStr   | SqlStmt_PrepareStr    |
| SQL->StmtPrepareV     | SqlStmt_PrepareV      |
| SQL->StmtShowDebug\_  | SqlStmt_ShowDebug\_   |

### strlib

[Back to Table of Contents](#toc "wikilink")

| Interface Name                | Function Name        |
|-------------------------------|----------------------|
| strlib->jstrescape           | jstrescape            |
| strlib->jmemescapecpy        | jmemescapecpy         |
| strlib->remove_control_chars | remove_control_chars  |
| strlib->trim                 | trim                  |
| strlib->normalize_name       | normalize_name        |
| strlib->stristr              | stristr               |
| strlib->e_mail_check         | e_mail_check          |
| strlib->config_switch        | config_switch         |
| strlib->safestrncpy          | safestrncpy           |
| strlib->safestrnlen          | safestrnlen           |
| strlib->safesnprintf         | safesnprintf          |
| strlib->strline              | strline               |
| strlib->bin2hex              | bin2hex               |
|                               |                      |

### SV

[Back to Table of Contents](#toc "wikilink")

| Interface Name      | Function Name  |
|---------------------|----------------|
| sv->parse_next     | sv_parse_next   |
| sv->parse          | sv_parse        |
| sv->split          | sv_split        |
| sv->escape_c       | sv_escape_c     |
| sv->unescape_c     | sv_unescape_c   |
| sv->skip_escaped_c | skip_escaped_c  |
| sv->readdb         | sv_readdb       |

### StrBuf

[Back to Table of Contents](#toc "wikilink")

| Interface Name     | Function Name       |
|--------------------|---------------------|
| StrBuf->Malloc    | StringBuf_Malloc     |
| StrBuf->Init      | StringBuf_Init       |
| StrBuf->Printf    | StringBuf_Printf     |
| StrBuf->Vprintf   | StringBuf_Vprintf    |
| StrBuf->Append    | StringBuf_Append     |
| StrBuf->AppendStr | StringBuf_AppendStr  |
| StrBuf->Length    | StringBuf_Length     |
| StrBuf->Value     | StringBuf_Value      |
| StrBuf->Clear     | StringBuf_Clear      |
| StrBuf->Destroy   | StringBuf_Destroy    |
| StrBuf->Free      | StringBuf_Free       |

### iTimer

[Back to Table of Contents](#toc "wikilink")

| Interface Name               | Function Name         | Past/Other emulators name |
|------------------------------|-----------------------|---------------------------|
| iTimer->gettick             | timer_gettick         | gettick                    |
| iTimer->gettick_nocache     | timer_gettick_nocache |                            |
| iTimer->add_timer           | timer_add             | add_timer                  |
| iTimer->add_timer_interval  | timer_add_interval    | add_timer_interval         |
| iTimer->add_timer_func_list | timer_add_func_list   | add_timer_func_list        |
| iTimer->get_timer           | timer_get             |                            |
| iTimer->delete_timer        | timer_do_delete       |                            |
| iTimer->addtick_timer       | timer_addtick         |                            |
| iTimer->settick_timer       | timer_settick         |                            |
| iTimer->get_uptime          | timer_get_uptime      |                            |
| iTimer->do_timer            | do_timer              |                            |
| iTimer->init                | timer_init            |                            |
| iTimer->final               | timer_final           |                            |

## Map Server

### Atcommand

[Back to Table of Contents](#toc "wikilink")

| Interface Name              | Function Name            |
|-----------------------------|--------------------------|
| atcommand->init            | do_init_atcommand         |
| atcommand->final           | do_final_atcommand        |
| atcommand->parse           | is_atcommand              |
| atcommand->can_use         | atcommand_can_use         |
| atcommand->can_use2        | atcommand_can_use2        |
| atcommand->create          | atcommand_hp_add          |
| atcommand->load_groups     | atcommand_db_load_groups  |
| atcommand->exists          | atcommand_exists          |
| atcommand->msg_read        | msg_config_read           |
| atcommand->final_msg       | do_final_msg              |
| atcommand->get_bind_byname | get_atcommandbind_byname  |

### Battle

[Back to Table of Contents](#toc "wikilink")

| Interface Name               | Function Name              |
|------------------------------|----------------------------|
| battle->bc                  | &battle_config              |
| battle->init                | do_init_battle              |
| battle->final               | do_final_battle             |
| battle->calc_attack         | battle_calc_attack          |
| battle->calc_damage         | battle_calc_damage          |
| battle->calc_gvg_damage     | battle_calc_gvg_damage      |
| battle->calc_bg_damage      | battle_calc_bg_damage       |
| battle->calc_base_damage    | battle_calc_base_damage     |
| battle->calc_misc_attack    | battle_calc_misc_attack     |
| battle->calc_magic_attack   | battle_calc_magic_attack    |
| battle->weapon_attack       | battle_weapon_attack        |
| battle->delay_damage        | battle_delay_damage         |
| battle->drain               | battle_drain                |
| battle->calc_return_damage  | battle_calc_return_damage   |
| battle->calc_weapon_attack  | battle_calc_weapon_attack   |
| battle->attr_ratio          | battle_attr_ratio           |
| battle->attr_fix            | battle_attr_fix             |
| battle->calc_cardfix        | battle_calc_cardfix         |
| battle->get_master          | battle_get_master           |
| battle->get_targeted        | battle_gettargeted          |
| battle->get_enemy           | battle_getenemy             |
| battle->get_target          | battle_gettarget            |
| battle->get_current_skill   | battle_getcurrentskill      |
| battle->check_undead        | battle_check_undead         |
| battle->check_target        | battle_check_target         |
| battle->check_range         | battle_check_range          |
| battle->consume_ammo        | battle_consume_ammo         |
| battle->get_targeted_sub    | battle_gettargeted_sub      |
| battle->get_enemy_sub       | battle_getenemy_sub         |
| battle->get_enemy_area_sub  | battle_getenemyarea_sub     |
| battle->delay_damage_sub    | battle_delay_damage_sub     |
| battle->blewcount_bonus     | battle_blewcount_bonus      |
| battle->range_type          | battle_range_type           |
| battle->adjust_skill_damage | battle_adjust_skill_damage  |
| battle->add_mastery         | battle_addmastery           |
| battle->calc_drain          | battle_calc_drain           |
| battle->config_read         | battle_config_read          |
| battle->config_set_defaults | battle_set_defaults         |
| battle->config_set_value    | battle_set_value            |
| battle->config_get_value    | battle_get_value            |
| battle->config_adjust       | battle_adjust_conf          |
| battle->get_enemy_area      | battle_getenemyarea         |
| battle->damage_area         | battle_damage_area          |

### Buyingstore

[Back to Table of Contents](#toc "wikilink")

| Interface Name          | Function Name         |
|-------------------------|-----------------------|
| buyingstore->setup     | buyingstore_setup      |
| buyingstore->create    | buyingstore_create     |
| buyingstore->close     | buyingstore_close      |
| buyingstore->open      | buyingstore_open       |
| buyingstore->trade     | buyingstore_trade      |
| buyingstore->search    | buyingstore_search     |
| buyingstore->searchall | buyingstore_searchall  |

### Clif

#### Core

[Back to Table of Contents](#toc "wikilink")

| Interface Name    | Function Name   |
|-------------------|-----------------|
| clif->init       | do_init_clif     |
| clif->final      | do_final_clif    |
| clif->setip      | clif_setip       |
| clif->setbindip  | clif_setbindip   |
| clif->setport    | clif_setport     |
| clif->refresh_ip | clif_refresh_ip  |
| clif->send       | clif_send        |
| clif->send_sub   | clif_send_sub    |
| clif->parse      | clif_parse       |

#### Auth

[Back to Table of Contents](#toc "wikilink")

| Interface Name      | Function Name     |
|---------------------|-------------------|
| clif->authok       | clif_authok        |
| clif->authrefuse   | clif_authrefuse    |
| clif->authfail_fd  | clif_authfail_fd   |
| clif->charselectok | clif_charselectok  |

#### Items

[Back to Table of Contents](#toc "wikilink")

| Interface Name          | Function Name         |
|-------------------------|-----------------------|
| clif->dropflooritem    | clif_dropflooritem     |
| clif->clearflooritem   | clif_clearflooritem    |
| clif->additem          | clif_additem           |
| clif->dropitem         | clif_dropitem          |
| clif->delitem          | clif_delitem           |
| clif->takeitem         | clif_takeitem          |
| clif->arrowequip       | clif_arrowequip        |
| clif->arrow_fail       | clif_arrow_fail        |
| clif->use_card         | clif_use_card          |
| clif->cart_additem     | clif_cart_additem      |
| clif->cart_delitem     | clif_cart_delitem      |
| clif->equipitemack     | clif_equipitemack      |
| clif->unequipitemack   | clif_unequipitemack    |
| clif->useitemack       | clif_useitemack        |
| clif->addcards         | clif_addcards          |
| clif->addcards2        | clif_addcards2         |
| clif->item_sub         | clif_item_sub          |
| clif->getareachar_item | clif_getareachar_item  |
| clif->rental_time      | clif_rental_time       |
| clif->rental_expired   | clif_rental_expired    |

#### Unit

[Back to Table of Contents](#toc "wikilink")

| Interface Name               | Function Name              |
|------------------------------|----------------------------|
| clif->clearunit_single      | clif_clearunit_single       |
| clif->clearunit_area        | clif_clearunit_area         |
| clif->clearunit_delayed     | clif_clearunit_delayed      |
| clif->walkok                | clif_walkok                 |
| clif->move                  | clif_move                   |
| clif->move2                 | clif_move2                  |
| clif->blown                 | clif_blown                  |
| clif->slide                 | clif_slide                  |
| clif->fixpos                | clif_fixpos                 |
| clif->changelook            | clif_changelook             |
| clif->changetraplook        | clif_changetraplook         |
| clif->refreshlook           | clif_refreshlook            |
| clif->class_change          | clif_class_change           |
| clif->skill_setunit         | clif_skill_setunit          |
| clif->skill_delunit         | clif_skill_delunit          |
| clif->skillunit_update      | clif_skillunit_update       |
| clif->clearunit_delayed_sub | clif_clearunit_delayed_sub  |
| clif->set_unit_idle         | clif_set_unit_idle          |
| clif->spawn_unit            | clif_spawn_unit             |
| clif->set_unit_walking      | clif_set_unit_walking       |
| clif->calc_walkdelay        | clif_calc_walkdelay         |
| clif->getareachar_skillunit | clif_getareachar_skillunit  |
| clif->getareachar_unit      | clif_getareachar_unit       |
| clif->clearchar_skillunit   | clif_clearchar_skillunit    |
| clif->getareachar           | clif_getareachar            |
| clif->spawn                 | clif_spawn                  |

#### Map

[Back to Table of Contents](#toc "wikilink")

| Interface Name             | Function Name            |
|----------------------------|--------------------------|
| clif->changemap           | clif_changemap            |
| clif->changemapcell       | clif_changemapcell        |
| clif->map_property        | clif_map_property         |
| clif->pvpset              | clif_pvpset               |
| clif->map_property_mapall | clif_map_property_mapall  |
| clif->bossmapinfo         | clif_bossmapinfo          |
| clif->map_type            | clif_map_type             |
| clif->maptypeproperty2    | clif_maptypeproperty2     |
| clif->changemapserver     | clif_changemapserver      |

#### NPC Shop

[Back to Table of Contents](#toc "wikilink")

| Interface Name         | Function Name        |
|------------------------|----------------------|
| clif->npcbuysell      | clif_npcbuysell       |
| clif->buylist         | clif_buylist          |
| clif->selllist        | clif_selllist         |
| clif->cashshop_show   | clif_cashshop_show    |
| clif->npc_buy_result  | clif_npc_buy_result   |
| clif->npc_sell_result | clif_npc_sell_result  |
| clif->cashshop_ack    | clif_cashshop_ack     |

#### NPC Script

[Back to Table of Contents](#toc "wikilink")

| Interface Name        | Function Name       |
|-----------------------|---------------------|
| clif->scriptmes      | clif_scriptmes       |
| clif->scriptnext     | clif_scriptnext      |
| clif->scriptclose    | clif_scriptclose     |
| clif->scriptmenu     | clif_scriptmenu      |
| clif->scriptinput    | clif_scriptinput     |
| clif->scriptinputstr | clif_scriptinputstr  |
| clif->cutin          | clif_cutin           |
| clif->sendfakenpc    | clif_sendfakenpc     |
| clif->scriptclear    | clif_scriptclear     |

#### Client User Interface

[Back to Table of Contents](#toc "wikilink")

| Interface Name                 | Function Name                |
|--------------------------------|------------------------------|
| clif->viewpoint               | clif_viewpoint                |
| clif->damage                  | clif_damage                   |
| clif->sitting                 | clif_sitting                  |
| clif->standing                | clif_standing                 |
| clif->arrow_create_list       | clif_arrow_create_list        |
| clif->refresh                 | clif_refresh                  |
| clif->fame_blacksmith         | clif_fame_blacksmith          |
| clif->fame_alchemist          | clif_fame_alchemist           |
| clif->fame_taekwon            | clif_fame_taekwon             |
| clif->hotkeys                 | clif_hotkeys_send             |
| clif->insight                 | clif_insight                  |
| clif->outsight                | clif_outsight                 |
| clif->skillcastcancel         | clif_skillcastcancel          |
| clif->skill_fail              | clif_skill_fail               |
| clif->skill_cooldown          | clif_skill_cooldown           |
| clif->skill_memomessage       | clif_skill_memomessage        |
| clif->skill_teleportmessage   | clif_skill_teleportmessage    |
| clif->skill_produce_mix_list  | clif_skill_produce_mix_list   |
| clif->cooking_list            | clif_cooking_list             |
| clif->autospell               | clif_autospell                |
| clif->combo_delay             | clif_combo_delay              |
| clif->status_change           | clif_status_change            |
| clif->insert_card             | clif_insert_card              |
| clif->inventorylist           | clif_inventorylist            |
| clif->equiplist               | clif_equiplist                |
| clif->cartlist                | clif_cartlist                 |
| clif->favorite_item           | clif_favorite_item            |
| clif->clearcart               | clif_clearcart                |
| clif->item_identify_list      | clif_item_identify_list       |
| clif->item_identified         | clif_item_identified          |
| clif->item_repair_list        | clif_item_repair_list         |
| clif->item_repaireffect       | clif_item_repaireffect        |
| clif->item_damaged            | clif_item_damaged             |
| clif->item_refine_list        | clif_item_refine_list         |
| clif->item_skill              | clif_item_skill               |
| clif->mvp_item                | clif_mvp_item                 |
| clif->mvp_exp                 | clif_mvp_exp                  |
| clif->mvp_noitem              | clif_mvp_noitem               |
| clif->changed_dir             | clif_changed_dir              |
| clif->charnameack             | clif_charnameack              |
| clif->monster_hp_bar          | clif_monster_hp_bar           |
| clif->hpmeter                 | clif_hpmeter                  |
| clif->hpmeter_single          | clif_hpmeter_single           |
| clif->hpmeter_sub             | clif_hpmeter_sub              |
| clif->upgrademessage          | clif_upgrademessage           |
| clif->get_weapon_view         | clif_get_weapon_view          |
| clif->gospel_info             | clif_gospel_info              |
| clif->feel_req                | clif_feel_req                 |
| clif->starskill               | clif_starskill                |
| clif->feel_info               | clif_feel_info                |
| clif->hate_info               | clif_hate_info                |
| clif->mission_info            | clif_mission_info             |
| clif->feel_hate_reset         | clif_feel_hate_reset          |
| clif->partytickack            | clif_partytickack             |
| clif->equiptickack            | clif_equiptickack             |
| clif->viewequip_ack           | clif_viewequip_ack            |
| clif->viewequip_fail          | clif_viewequip_fail           |
| clif->equpcheckbox            | clif_equpcheckbox             |
| clif->displayexp              | clif_displayexp               |
| clif->font                    | clif_font                     |
| clif->progressbar             | clif_progressbar              |
| clif->progressbar_abort       | clif_progressbar_abort        |
| clif->showdigit               | clif_showdigit                |
| clif->elementalconverter_list | clif_elementalconverter_list  |
| clif->spellbook_list          | clif_spellbook_list           |
| clif->magicdecoy_list         | clif_magicdecoy_list          |
| clif->poison_list             | clif_poison_list              |
| clif->autoshadowspell_list    | clif_autoshadowspell_list     |
| clif->skill_itemlistwindow    | clif_skill_itemlistwindow     |
| clif->sc_load                 | clif_status_change2           |
| clif->sc_end                  | clif_status_change_end        |
| clif->initialstatus           | clif_initialstatus            |

#### Player Unit

[Back to Table of Contents](#toc "wikilink")

| Interface Name         | Function Name        |
|------------------------|----------------------|
| clif->updatestatus    | clif_updatestatus     |
| clif->changestatus    | clif_changestatus     |
| clif->statusupack     | clif_statusupack      |
| clif->movetoattack    | clif_movetoattack     |
| clif->solved_charname | clif_solved_charname  |
| clif->charnameupdate  | clif_charnameupdate   |
| clif->delayquit       | clif_delayquit        |
| clif->getareachar_pc  | clif_getareachar_pc   |
| clif->disconnect_ack  | clif_disconnect_ack   |
| clif->PVPInfo         | clif_PVPInfo          |
| clif->blacksmith      | clif_blacksmith       |
| clif->alchemist       | clif_alchemist        |
| clif->taekwon         | clif_taekwon          |
| clif->ranking_pk      | clif_ranking_pk       |
| clif->quitsave        | clif_quitsave         |

#### Effects

[Back to Table of Contents](#toc "wikilink")

| Interface Name              | Function Name             |
|-----------------------------|---------------------------|
| clif->misceffect           | clif_misceffect            |
| clif->changeoption         | clif_changeoption          |
| clif->changeoption2        | clif_changeoption2         |
| clif->emotion              | clif_emotion               |
| clif->talkiebox            | clif_talkiebox             |
| clif->wedding_effect       | clif_wedding_effect        |
| clif->divorced             | clif_divorced              |
| clif->callpartner          | clif_callpartner           |
| clif->skill_damage         | clif_skill_damage          |
| clif->skill_nodamage       | clif_skill_nodamage        |
| clif->skill_poseffect      | clif_skill_poseffect       |
| clif->skill_estimation     | clif_skill_estimation      |
| clif->skill_warppoint      | clif_skill_warppoint       |
| clif->skillcasting         | clif_skillcasting          |
| clif->produce_effect       | clif_produceeffect         |
| clif->devotion             | clif_devotion              |
| clif->spiritball           | clif_spiritball            |
| clif->spiritball_single    | clif_spiritball_single     |
| clif->bladestop            | clif_bladestop             |
| clif->mvp_effect           | clif_mvp_effect            |
| clif->heal                 | clif_heal                  |
| clif->resurrection         | clif_resurrection          |
| clif->refine               | clif_refine                |
| clif->weather              | clif_weather               |
| clif->specialeffect        | clif_specialeffect         |
| clif->specialeffect_single | clif_specialeffect_single  |
| clif->specialeffect_value  | clif_specialeffect_value   |
| clif->millenniumshield     | clif_millenniumshield      |
| clif->talisman             | clif_talisman              |
| clif->talisman_single      | clif_talisman_single       |
| clif->snap                 | clif_snap                  |
| clif->weather_check        | clif_weather_check         |
| clif->playBGM              | clif_playBGM               |
| clif->soundeffect          | clif_soundeffect           |
| clif->soundeffectall       | clif_soundeffectall        |

#### Chat/Messages

[Back to Table of Contents](#toc "wikilink")

| Interface Name          | Function Name         |
|-------------------------|-----------------------|
| clif->GlobalMessage    | clif_GlobalMessage     |
| clif->createchat       | clif_createchat        |
| clif->dispchat         | clif_dispchat          |
| clif->joinchatfail     | clif_joinchatfail      |
| clif->joinchatok       | clif_joinchatok        |
| clif->addchat          | clif_addchat           |
| clif->changechatowner  | clif_changechatowner   |
| clif->clearchat        | clif_clearchat         |
| clif->leavechat        | clif_leavechat         |
| clif->changechatstatus | clif_changechatstatus  |
| clif->wis_message      | clif_wis_message       |
| clif->wis_end          | clif_wis_end           |
| clif->disp_onlyself    | clif_disp_onlyself     |
| clif->disp_message     | clif_disp_message      |
| clif->broadcast        | clif_broadcast         |
| clif->broadcast2       | clif_broadcast2        |
| clif->messagecolor     | clif_messagecolor      |
| clif->disp_overhead    | clif_disp_overhead     |
| clif->msg              | clif_msg               |
| clif->msg_value        | clif_msg_value         |
| clif->msg_skill        | clif_msg_skill         |
| clif->msgtable         | clif_msgtable          |
| clif->msgtable_num     | clif_msgtable_num      |
| clif->message          | clif_displaymessage    |
| clif->messageln        | clif_displaymessage2   |
| clif->colormes         | clif_colormes          |
| clif->process_message  | clif_process_message   |
| clif->wisexin          | clif_wisexin           |
| clif->wisall           | clif_wisall            |
| clif->PMIgnoreList     | clif_PMIgnoreList      |

#### Trade

[Back to Table of Contents](#toc "wikilink")

| Interface Name        | Function Name       |
|-----------------------|---------------------|
| clif->traderequest   | clif_traderequest    |
| clif->tradestart     | clif_tradestart      |
| clif->tradeadditem   | clif_tradeadditem    |
| clif->tradeitemok    | clif_tradeitemok     |
| clif->tradedeal_lock | clif_tradedeal_lock  |
| clif->tradecancelled | clif_tradecancelled  |
| clif->tradecompleted | clif_tradecompleted  |
| clif->tradeundo      | clif_tradeundo       |

#### Vending

[Back to Table of Contents](#toc "wikilink")

| Interface Name           | Function Name          |
|--------------------------|------------------------|
| clif->openvendingreq    | clif_openvendingreq     |
| clif->showvendingboard  | clif_showvendingboard   |
| clif->closevendingboard | clif_closevendingboard  |
| clif->vendinglist       | clif_vendinglist        |
| clif->buyvending        | clif_buyvending         |
| clif->openvending       | clif_openvending        |
| clif->vendingreport     | clif_vendingreport      |

#### Storage

[Back to Table of Contents](#toc "wikilink")

| Interface Name             | Function Name            |
|----------------------------|--------------------------|
| clif->storagelist         | clif_storagelist          |
| clif->updatestorageamount | clif_updatestorageamount  |
| clif->storageitemadded    | clif_storageitemadded     |
| clif->storageitemremoved  | clif_storageitemremoved   |
| clif->storageclose        | clif_storageclose         |

#### Skill List

[Back to Table of Contents](#toc "wikilink")

| Interface Name        | Function Name       |
|-----------------------|---------------------|
| clif->skillinfoblock | clif_skillinfoblock  |
| clif->skillup        | clif_skillup         |
| clif->skillinfo      | clif_skillinfo       |
| clif->addskill       | clif_addskill        |
| clif->deleteskill    | clif_deleteskill     |

#### Party

[Back to Table of Contents](#toc "wikilink")

| Interface Name              | Function Name             |
|-----------------------------|---------------------------|
| clif->party_created        | clif_party_created         |
| clif->party_member_info    | clif_party_member_info     |
| clif->party_info           | clif_party_info            |
| clif->party_invite         | clif_party_invite          |
| clif->party_inviteack      | clif_party_inviteack       |
| clif->party_option         | clif_party_option          |
| clif->party_withdraw       | clif_party_withdraw        |
| clif->party_message        | clif_party_message         |
| clif->party_xy             | clif_party_xy              |
| clif->party_xy_single      | clif_party_xy_single       |
| clif->party_hp             | clif_party_hp              |
| clif->party_xy_remove      | clif_party_xy_remove       |
| clif->party_show_picker    | clif_party_show_picker     |
| clif->partyinvitationstate | clif_partyinvitationstate  |

#### Guild

[Back to Table of Contents](#toc "wikilink")

| Interface Name                     | Function Name                    |
|------------------------------------|----------------------------------|
| clif->guild_created               | clif_guild_created                |
| clif->guild_belonginfo            | clif_guild_belonginfo             |
| clif->guild_masterormember        | clif_guild_masterormember         |
| clif->guild_basicinfo             | clif_guild_basicinfo              |
| clif->guild_allianceinfo          | clif_guild_allianceinfo           |
| clif->guild_memberlist            | clif_guild_memberlist             |
| clif->guild_skillinfo             | clif_guild_skillinfo              |
| clif->guild_send_onlineinfo       | clif_guild_send_onlineinfo        |
| clif->guild_memberlogin_notice    | clif_guild_memberlogin_notice     |
| clif->guild_invite                | clif_guild_invite                 |
| clif->guild_inviteack             | clif_guild_inviteack              |
| clif->guild_leave                 | clif_guild_leave                  |
| clif->guild_expulsion             | clif_guild_expulsion              |
| clif->guild_positionchanged       | clif_guild_positionchanged        |
| clif->guild_memberpositionchanged | clif_guild_memberpositionchanged  |
| clif->guild_emblem                | clif_guild_emblem                 |
| clif->guild_emblem_area           | clif_guild_emblem_area            |
| clif->guild_notice                | clif_guild_notice                 |
| clif->guild_message               | clif_guild_message                |
| clif->guild_skillup               | clif_guild_skillup                |
| clif->guild_reqalliance           | clif_guild_reqalliance            |
| clif->guild_allianceack           | clif_guild_allianceack            |
| clif->guild_delalliance           | clif_guild_delalliance            |
| clif->guild_oppositionack         | clif_guild_oppositionack          |
| clif->guild_broken                | clif_guild_broken                 |
| clif->guild_xy                    | clif_guild_xy                     |
| clif->guild_xy_single             | clif_guild_xy_single              |
| clif->guild_xy_remove             | clif_guild_xy_remove              |
| clif->guild_positionnamelist      | clif_guild_positionnamelist       |
| clif->guild_positioninfolist      | clif_guild_positioninfolist       |
| clif->guild_expulsionlist         | clif_guild_expulsionlist          |
| clif->validate_emblem             | clif_validate_emblem              |

#### Battleground

[Back to Table of Contents](#toc "wikilink")

| Interface Name               | Function Name              |
|------------------------------|----------------------------|
| clif->bg_hp                 | clif_bg_hp                  |
| clif->bg_xy                 | clif_bg_xy                  |
| clif->bg_xy_remove          | clif_bg_xy_remove           |
| clif->bg_message            | clif_bg_message             |
| clif->bg_updatescore        | clif_bg_updatescore         |
| clif->bg_updatescore_single | clif_bg_updatescore_single  |
| clif->sendbgemblem_area     | clif_sendbgemblem_area      |
| clif->sendbgemblem_single   | clif_sendbgemblem_single    |
| clif->bgqueue_ack           | clif_bgqueue_ack            |
| clif->bgqueue_notice_delete | clif_bgqueue_notice_delete  |
| clif->bgqueue_update_info   | clif_bgqueue_update_info    |
| clif->bgqueue_joined        | clif_bgqueue_joined         |
| clif->bgqueue_pcleft        | clif_bgqueue_pcleft         |
| clif->bgqueue_battlebegins  | clif_bgqueue_battlebegins   |
|                              |                            |

#### Instance

[Back to Table of Contents](#toc "wikilink")

| Interface Name        | Function Name       |
|-----------------------|---------------------|
| clif->instance       | clif_instance        |
| clif->instance_join  | clif_instance_join   |
| clif->instance_leave | clif_instance_leave  |

#### Pet

[Back to Table of Contents](#toc "wikilink")

| Interface Name        | Function Name       |
|-----------------------|---------------------|
| clif->catch_process  | clif_catch_process   |
| clif->pet_roulette   | clif_pet_roulette    |
| clif->sendegg        | clif_sendegg         |
| clif->send_petstatus | clif_send_petstatus  |
| clif->send_petdata   | clif_send_petdata    |
| clif->pet_emotion    | clif_pet_emotion     |
| clif->pet_food       | clif_pet_food        |

#### Friend

[Back to Table of Contents](#toc "wikilink")

| Interface Name                | Function Name               |
|-------------------------------|-----------------------------|
| clif->friendslist_toggle_sub | clif_friendslist_toggle_sub  |
| clif->friendslist_send       | clif_friendslist_send        |
| clif->friendslist_reqack     | clif_friendslist_reqack      |
| clif->friendslist_toggle     | clif_friendslist_toggle      |
| clif->friendlist_req         | clif_friendlist_req          |

#### GM

[Back to Table of Contents](#toc "wikilink")

| Interface Name        | Function Name       |
|-----------------------|---------------------|
| clif->GM_kickack     | clif_GM_kickack      |
| clif->GM_kick        | clif_GM_kick         |
| clif->manner_message | clif_manner_message  |
| clif->GM_silence     | clif_GM_silence      |
| clif->account_name   | clif_account_name    |
| clif->check          | clif_check           |

#### Homunculus

[Back to Table of Contents](#toc "wikilink")

| Interface Name           | Function Name          |
|--------------------------|------------------------|
| clif->hominfo           | clif_hominfo            |
| clif->homskillinfoblock | clif_homskillinfoblock  |
| clif->homskillup        | clif_homskillup         |
| clif->hom_food          | clif_hom_food           |
| clif->send_homdata      | clif_send_homdata       |

#### Quest Log

[Back to Table of Contents](#toc "wikilink")

| Interface Name                | Function Name               |
|-------------------------------|-----------------------------|
| clif->quest_send_list        | clif_quest_send_list         |
| clif->quest_send_mission     | clif_quest_send_mission      |
| clif->quest_add              | clif_quest_add               |
| clif->quest_delete           | clif_quest_delete            |
| clif->quest_update_status    | clif_quest_update_status     |
| clif->quest_update_objective | clif_quest_update_objective  |
| clif->quest_show_event       | clif_quest_show_event        |

#### Mail

[Back to Table of Contents](#toc "wikilink")

| Interface Name            | Function Name           |
|---------------------------|-------------------------|
| clif->mail_window        | clif_Mail_window         |
| clif->mail_read          | clif_Mail_read           |
| clif->mail_delete        | clif_Mail_delete         |
| clif->mail_return        | clif_Mail_return         |
| clif->mail_send          | clif_Mail_send           |
| clif->mail_new           | clif_Mail_new            |
| clif->mail_refreshinbox  | clif_Mail_refreshinbox   |
| clif->mail_getattachment | clif_Mail_getattachment  |
| clif->mail_setattachment | clif_Mail_setattachment  |

#### Auction

[Back to Table of Contents](#toc "wikilink")

| Interface Name            | Function Name           |
|---------------------------|-------------------------|
| clif->auction_openwindow | clif_Auction_openwindow  |
| clif->auction_results    | clif_Auction_results     |
| clif->auction_message    | clif_Auction_message     |
| clif->auction_close      | clif_Auction_close       |
| clif->auction_setitem    | clif_Auction_setitem     |

#### Mercenary

[Back to Table of Contents](#toc "wikilink")

| Interface Name                | Function Name               |
|-------------------------------|-----------------------------|
| clif->mercenary_info         | clif_mercenary_info          |
| clif->mercenary_skillblock   | clif_mercenary_skillblock    |
| clif->mercenary_message      | clif_mercenary_message       |
| clif->mercenary_updatestatus | clif_mercenary_updatestatus  |

#### Party Booking/Group Search

[Back to Table of Contents](#toc "wikilink")

| Interface Name                      | Function Name                     |
|-------------------------------------|-----------------------------------|
| clif->PartyBookingRegisterAck      | clif_PartyBookingRegisterAck       |
| clif->PartyBookingDeleteAck        | clif_PartyBookingDeleteAck         |
| clif->PartyBookingSearchAck        | clif_PartyBookingSearchAck         |
| clif->PartyBookingUpdateNotify     | clif_PartyBookingUpdateNotify      |
| clif->PartyBookingDeleteNotify     | clif_PartyBookingDeleteNotify      |
| clif->PartyBookingInsertNotify     | clif_PartyBookingInsertNotify      |
| clif->PartyBookingVolunteerInfo    | clif_PartyBookingVolunteerInfo     |
| clif->PartyBookingRefuseVolunteer  | clif_PartyBookingRefuseVolunteer   |
| clif->PartyBookingCancelVolunteer  | clif_PartyBookingCancelVolunteer   |
| clif->PartyBookingAddFilteringList | clif_PartyBookingAddFilteringList  |
| clif->PartyBookingSubFilteringList | clif_PartyBookingSubFilteringList  |

#### Buying Store

[Back to Table of Contents](#toc "wikilink")

| Interface Name                            | Function Name                           |
|-------------------------------------------|-----------------------------------------|
| clif->buyingstore_open                   | clif_buyingstore_open                    |
| clif->buyingstore_open_failed            | clif_buyingstore_open_failed             |
| clif->buyingstore_myitemlist             | clif_buyingstore_myitemlist              |
| clif->buyingstore_entry                  | clif_buyingstore_entry                   |
| clif->buyingstore_entry_single           | clif_buyingstore_entry_single            |
| clif->buyingstore_disappear_entry        | clif_buyingstore_disappear_entry         |
| clif->buyingstore_disappear_entry_single | clif_buyingstore_disappear_entry_single  |
| clif->buyingstore_itemlist               | clif_buyingstore_itemlist                |
| clif->buyingstore_trade_failed_buyer     | clif_buyingstore_trade_failed_buyer      |
| clif->buyingstore_update_item            | clif_buyingstore_update_item             |
| clif->buyingstore_delete_item            | clif_buyingstore_delete_item             |
| clif->buyingstore_trade_failed_seller    | clif_buyingstore_trade_failed_seller     |

#### Search Store

[Back to Table of Contents](#toc "wikilink")

| Interface Name                     | Function Name                    |
|------------------------------------|----------------------------------|
| clif->search_store_info_ack       | clif_search_store_info_ack        |
| clif->search_store_info_failed    | clif_search_store_info_failed     |
| clif->open_search_store_info      | clif_open_search_store_info       |
| clif->search_store_info_click_ack | clif_search_store_info_click_ack  |

#### Elemental

[Back to Table of Contents](#toc "wikilink")

| Interface Name                | Function Name               |
|-------------------------------|-----------------------------|
| clif->elemental_info         | clif_elemental_info          |
| clif->elemental_updatestatus | clif_elemental_updatestatus  |

#### Hercules Channel System

[Back to Table of Contents](#toc "wikilink")

| Interface Name      | Function Name              |
|---------------------|----------------------------|
| clif->chsys_create | clif_hercules_chsys_create  |
| clif->chsys_msg    | clif_hercules_chsys_msg     |
| clif->chsys_msg2   | clif_hercules_chsys_msg2    |
| clif->chsys_send   | clif_hercules_chsys_send    |
| clif->chsys_join   | clif_hercules_chsys_join    |
| clif->chsys_left   | clif_hercules_chsys_left    |
| clif->chsys_delete | clif_hercules_chsys_delete  |
| clif->chsys_mjoin  | clif_hercules_chsys_mjoin   |
| clif->chsys_quit   | clif_hercules_chsys_quit    |
| clif->chsys_quitg  | clif_hercules_chsys_quitg   |
| clif->chsys_gjoin  | clif_hercules_chsys_gjoin   |
| clif->chsys_gleave | clif_hercules_chsys_gleave  |

#### Miscellaneous

[Back to Table of Contents](#toc "wikilink")

| Interface Name          | Function Name         |
|-------------------------|-----------------------|
| clif->adopt_reply      | clif_Adopt_reply       |
| clif->adopt_request    | clif_Adopt_request     |
| clif->readbook         | clif_readbook          |
| clif->notify_time      | clif_notify_time       |
| clif->user_count       | clif_user_count        |
| clif->noask_sub        | clif_noask_sub         |
| clif->cashshop_load    | clif_cashshop_db       |
| clif->bc_ready         | clif_bc_ready          |
| clif->undisguise_timer | clif_undisguise_timer  |

#### Parse Incoming Pckets

[Back to Table of Contents](#toc "wikilink")

| Interface Name                       | Function Name                           |
|--------------------------------------|-----------------------------------------|
| clif->pWantToConnection             | clif_parse_WantToConnection              |
| clif->pLoadEndAck                   | clif_parse_LoadEndAck                    |
| clif->pTickSend                     | clif_parse_TickSend                      |
| clif->pHotkey                       | clif_parse_Hotkey                        |
| clif->pProgressbar                  | clif_parse_progressbar                   |
| clif->pWalkToXY                     | clif_parse_WalkToXY                      |
| clif->pQuitGame                     | clif_parse_QuitGame                      |
| clif->pGetCharNameRequest           | clif_parse_GetCharNameRequest            |
| clif->pGlobalMessage                | clif_parse_GlobalMessage                 |
| clif->pMapMove                      | clif_parse_MapMove                       |
| clif->pChangeDir                    | clif_parse_ChangeDir                     |
| clif->pEmotion                      | clif_parse_Emotion                       |
| clif->pHowManyConnections           | clif_parse_HowManyConnections            |
| clif->pActionRequest                | clif_parse_ActionRequest                 |
| clif->pActionRequest_sub            | clif_parse_ActionRequest_sub             |
| clif->pRestart                      | clif_parse_Restart                       |
| clif->pWisMessage                   | clif_parse_WisMessage                    |
| clif->pBroadcast                    | clif_parse_Broadcast                     |
| clif->pTakeItem                     | clif_parse_TakeItem                      |
| clif->pDropItem                     | clif_parse_DropItem                      |
| clif->pUseItem                      | clif_parse_UseItem                       |
| clif->pEquipItem                    | clif_parse_EquipItem                     |
| clif->pUnequipItem                  | clif_parse_UnequipItem                   |
| clif->pNpcClicked                   | clif_parse_NpcClicked                    |
| clif->pNpcBuySellSelected           | clif_parse_NpcBuySellSelected            |
| clif->pNpcBuyListSend               | clif_parse_NpcBuyListSend                |
| clif->pNpcSellListSend              | clif_parse_NpcSellListSend               |
| clif->pCreateChatRoom               | clif_parse_CreateChatRoom                |
| clif->pChatAddMember                | clif_parse_ChatAddMember                 |
| clif->pChatRoomStatusChange         | clif_parse_ChatRoomStatusChange          |
| clif->pChangeChatOwner              | clif_parse_ChangeChatOwner               |
| clif->pKickFromChat                 | clif_parse_KickFromChat                  |
| clif->pChatLeave                    | clif_parse_ChatLeave                     |
| clif->pTradeRequest                 | clif_parse_TradeRequest                  |
| clif->pTradeAck                     | clif_parse_TradeAck                      |
| clif->pTradeAddItem                 | clif_parse_TradeAddItem                  |
| clif->pTradeOk                      | clif_parse_TradeOk                       |
| clif->pTradeCancel                  | clif_parse_TradeCancel                   |
| clif->pTradeCommit                  | clif_parse_TradeCommit                   |
| clif->pStopAttack                   | clif_parse_StopAttack                    |
| clif->pPutItemToCart                | clif_parse_PutItemToCart                 |
| clif->pGetItemFromCart              | clif_parse_GetItemFromCart               |
| clif->pRemoveOption                 | clif_parse_RemoveOption                  |
| clif->pChangeCart                   | clif_parse_ChangeCart                    |
| clif->pStatusUp                     | clif_parse_StatusUp                      |
| clif->pSkillUp                      | clif_parse_SkillUp                       |
| clif->pUseSkillToId                 | clif_parse_UseSkillToId                  |
| clif->pUseSkillToId_homun           | clif_parse_UseSkillToId_homun            |
| clif->pUseSkillToId_mercenary       | clif_parse_UseSkillToId_mercenary        |
| clif->pUseSkillToPos                | clif_parse_UseSkillToPos                 |
| clif->pUseSkillToPosSub             | clif_parse_UseSkillToPosSub              |
| clif->pUseSkillToPos_homun          | clif_parse_UseSkillToPos_homun           |
| clif->pUseSkillToPos_mercenary      | clif_parse_UseSkillToPos_mercenary       |
| clif->pUseSkillToPosMoreInfo        | clif_parse_UseSkillToPosMoreInfo         |
| clif->pUseSkillMap                  | clif_parse_UseSkillMap                   |
| clif->pRequestMemo                  | clif_parse_RequestMemo                   |
| clif->pProduceMix                   | clif_parse_ProduceMix                    |
| clif->pCooking                      | clif_parse_Cooking                       |
| clif->pRepairItem                   | clif_parse_RepairItem                    |
| clif->pWeaponRefine                 | clif_parse_WeaponRefine                  |
| clif->pNpcSelectMenu                | clif_parse_NpcSelectMenu                 |
| clif->pNpcNextClicked               | clif_parse_NpcNextClicked                |
| clif->pNpcAmountInput               | clif_parse_NpcAmountInput                |
| clif->pNpcStringInput               | clif_parse_NpcStringInput                |
| clif->pNpcCloseClicked              | clif_parse_NpcCloseClicked               |
| clif->pItemIdentify                 | clif_parse_ItemIdentify                  |
| clif->pSelectArrow                  | clif_parse_SelectArrow                   |
| clif->pAutoSpell                    | clif_parse_AutoSpell                     |
| clif->pUseCard                      | clif_parse_UseCard                       |
| clif->pInsertCard                   | clif_parse_InsertCard                    |
| clif->pSolveCharName                | clif_parse_SolveCharName                 |
| clif->pResetChar                    | clif_parse_ResetChar                     |
| clif->pLocalBroadcast               | clif_parse_LocalBroadcast                |
| clif->pMoveToKafra                  | clif_parse_MoveToKafra                   |
| clif->pMoveFromKafra                | clif_parse_MoveFromKafra                 |
| clif->pMoveToKafraFromCart          | clif_parse_MoveToKafraFromCart           |
| clif->pMoveFromKafraToCart          | clif_parse_MoveFromKafraToCart           |
| clif->pCloseKafra                   | clif_parse_CloseKafra                    |
| clif->pStoragePassword              | clif_parse_StoragePassword               |
| clif->pCreateParty                  | clif_parse_CreateParty                   |
| clif->pCreateParty2                 | clif_parse_CreateParty2                  |
| clif->pPartyInvite                  | clif_parse_PartyInvite                   |
| clif->pPartyInvite2                 | clif_parse_PartyInvite2                  |
| clif->pReplyPartyInvite             | clif_parse_ReplyPartyInvite              |
| clif->pReplyPartyInvite2            | clif_parse_ReplyPartyInvite2             |
| clif->pLeaveParty                   | clif_parse_LeaveParty                    |
| clif->pRemovePartyMember            | clif_parse_RemovePartyMember             |
| clif->pPartyChangeOption            | clif_parse_PartyChangeOption             |
| clif->chann_config_read             | read_channels_config                     |
| clif->pPartyMessage                 | clif_parse_PartyMessage                  |
| clif->pPartyChangeLeader            | clif_parse_PartyChangeLeader             |
| clif->pPartyBookingRegisterReq      | clif_parse_PartyBookingRegisterReq       |
| clif->pPartyBookingSearchReq        | clif_parse_PartyBookingSearchReq         |
| clif->pPartyBookingDeleteReq        | clif_parse_PartyBookingDeleteReq         |
| clif->pPartyBookingUpdateReq        | clif_parse_PartyBookingUpdateReq         |
| clif->pCloseVending                 | clif_parse_CloseVending                  |
| clif->pVendingListReq               | clif_parse_VendingListReq                |
| clif->pPurchaseReq                  | clif_parse_PurchaseReq                   |
| clif->pPurchaseReq2                 | clif_parse_PurchaseReq2                  |
| clif->pOpenVending                  | clif_parse_OpenVending                   |
| clif->pCreateGuild                  | clif_parse_CreateGuild                   |
| clif->pGuildCheckMaster             | clif_parse_GuildCheckMaster              |
| clif->pGuildRequestInfo             | clif_parse_GuildRequestInfo              |
| clif->pGuildChangePositionInfo      | clif_parse_GuildChangePositionInfo       |
| clif->pGuildChangeMemberPosition    | clif_parse_GuildChangeMemberPosition     |
| clif->pGuildRequestEmblem           | clif_parse_GuildRequestEmblem            |
| clif->pGuildChangeEmblem            | clif_parse_GuildChangeEmblem             |
| clif->pGuildChangeNotice            | clif_parse_GuildChangeNotice             |
| clif->pGuildInvite                  | clif_parse_GuildInvite                   |
| clif->pGuildReplyInvite             | clif_parse_GuildReplyInvite              |
| clif->pGuildLeave                   | clif_parse_GuildLeave                    |
| clif->pGuildExpulsion               | clif_parse_GuildExpulsion                |
| clif->pGuildMessage                 | clif_parse_GuildMessage                  |
| clif->pGuildRequestAlliance         | clif_parse_GuildRequestAlliance          |
| clif->pGuildReplyAlliance           | clif_parse_GuildReplyAlliance            |
| clif->pGuildDelAlliance             | clif_parse_GuildDelAlliance              |
| clif->pGuildOpposition              | clif_parse_GuildOpposition               |
| clif->pGuildBreak                   | clif_parse_GuildBreak                    |
| clif->pPetMenu                      | clif_parse_PetMenu                       |
| clif->pCatchPet                     | clif_parse_CatchPet                      |
| clif->pSelectEgg                    | clif_parse_SelectEgg                     |
| clif->pSendEmotion                  | clif_parse_SendEmotion                   |
| clif->pChangePetName                | clif_parse_ChangePetName                 |
| clif->pGMKick                       | clif_parse_GMKick                        |
| clif->pGMKickAll                    | clif_parse_GMKickAll                     |
| clif->pGMShift                      | clif_parse_GMShift                       |
| clif->pGMRemove2                    | clif_parse_GMRemove2                     |
| clif->pGMRecall                     | clif_parse_GMRecall                      |
| clif->pGMRecall2                    | clif_parse_GMRecall2                     |
| clif->pGM_Monster_Item              | clif_parse_GM_Monster_Item               |
| clif->pGMHide                       | clif_parse_GMHide                        |
| clif->pGMReqNoChat                  | clif_parse_GMReqNoChat                   |
| clif->pGMRc                         | clif_parse_GMRc                          |
| clif->pGMReqAccountName             | clif_parse_GMReqAccountName              |
| clif->pGMChangeMapType              | clif_parse_GMChangeMapType               |
| clif->pPMIgnore                     | clif_parse_PMIgnore                      |
| clif->pPMIgnoreAll                  | clif_parse_PMIgnoreAll                   |
| clif->pPMIgnoreList                 | clif_parse_PMIgnoreList                  |
| clif->pNoviceDoriDori               | clif_parse_NoviceDoriDori                |
| clif->pNoviceExplosionSpirits       | clif_parse_NoviceExplosionSpirits        |
| clif->pFriendsListAdd               | clif_parse_FriendsListAdd                |
| clif->pFriendsListReply             | clif_parse_FriendsListReply              |
| clif->pFriendsListRemove            | clif_parse_FriendsListRemove             |
| clif->pPVPInfo                      | clif_parse_PVPInfo                       |
| clif->pBlacksmith                   | clif_parse_Blacksmith                    |
| clif->pAlchemist                    | clif_parse_Alchemist                     |
| clif->pTaekwon                      | clif_parse_Taekwon                       |
| clif->pRankingPk                    | clif_parse_RankingPk                     |
| clif->pFeelSaveOk                   | clif_parse_FeelSaveOk                    |
| clif->pChangeHomunculusName         | clif_parse_ChangeHomunculusName          |
| clif->pHomMoveToMaster              | clif_parse_HomMoveToMaster               |
| clif->pHomMoveTo                    | clif_parse_HomMoveTo                     |
| clif->pHomAttack                    | clif_parse_HomAttack                     |
| clif->pHomMenu                      | clif_parse_HomMenu                       |
| clif->pAutoRevive                   | clif_parse_AutoRevive                    |
| clif->pCheck                        | clif_parse_Check                         |
| clif->pMail_refreshinbox            | clif_parse_Mail_refreshinbox             |
| clif->pMail_read                    | clif_parse_Mail_read                     |
| clif->pMail_getattach               | clif_parse_Mail_getattach                |
| clif->pMail_delete                  | clif_parse_Mail_delete                   |
| clif->pMail_return                  | clif_parse_Mail_return                   |
| clif->pMail_setattach               | clif_parse_Mail_setattach                |
| clif->pMail_winopen                 | clif_parse_Mail_winopen                  |
| clif->pMail_send                    | clif_parse_Mail_send                     |
| clif->pAuction_cancelreg            | clif_parse_Auction_cancelreg             |
| clif->pAuction_setitem              | clif_parse_Auction_setitem               |
| clif->pAuction_register             | clif_parse_Auction_register              |
| clif->pAuction_cancel               | clif_parse_Auction_cancel                |
| clif->pAuction_close                | clif_parse_Auction_close                 |
| clif->pAuction_bid                  | clif_parse_Auction_bid                   |
| clif->pAuction_search               | clif_parse_Auction_search                |
| clif->pAuction_buysell              | clif_parse_Auction_buysell               |
| clif->pcashshop_buy                 | clif_parse_cashshop_buy                  |
| clif->pAdopt_request                | clif_parse_Adopt_request                 |
| clif->pAdopt_reply                  | clif_parse_Adopt_reply                   |
| clif->pViewPlayerEquip              | clif_parse_ViewPlayerEquip               |
| clif->pEquipTick                    | clif_parse_EquipTick                     |
| clif->pquestStateAck                | clif_parse_questStateAck                 |
| clif->pmercenary_action             | clif_parse_mercenary_action              |
| clif->pBattleChat                   | clif_parse_BattleChat                    |
| clif->pLessEffect                   | clif_parse_LessEffect                    |
| clif->pItemListWindowSelected       | clif_parse_ItemListWindowSelected        |
| clif->pReqOpenBuyingStore           | clif_parse_ReqOpenBuyingStore            |
| clif->pReqCloseBuyingStore          | clif_parse_ReqCloseBuyingStore           |
| clif->pReqClickBuyingStore          | clif_parse_ReqClickBuyingStore           |
| clif->pReqTradeBuyingStore          | clif_parse_ReqTradeBuyingStore           |
| clif->pSearchStoreInfo              | clif_parse_SearchStoreInfo               |
| clif->pSearchStoreInfoNextPage      | clif_parse_SearchStoreInfoNextPage       |
| clif->pCloseSearchStoreInfo         | clif_parse_CloseSearchStoreInfo          |
| clif->pSearchStoreInfoListItemClick | clif_parse_SearchStoreInfoListItemClick  |
| clif->pDebug                        | clif_parse_debug                         |
| clif->pSkillSelectMenu              | clif_parse_SkillSelectMenu               |
| clif->pMoveItem                     | clif_parse_MoveItem                      |
| clif->pPartyTick                    | clif_parse_PartyTick                     |
| clif->pGuildInvite2                 | clif_parse_GuildInvite2                  |
| clif->pCashShopOpen                 | clif_parse_CashShopOpen                  |
| clif->pCashShopClose                | clif_parse_CashShopClose                 |
| clif->pCashShopReqTab               | clif_parse_CashShopReqTab                |
| clif->pCashShopSchedule             | clif_parse_CashShopSchedule              |
| clif->pCashShopBuy                  | clif_parse_CashShopBuy                   |
| clif->pPartyBookingAddFilter        | clif_parse_PartyBookingAddFilteringList  |
| clif->pPartyBookingSubFilter        | clif_parse_PartyBookingSubFilteringList  |
| clif->pPartyBookingReqVolunteer     | clif_parse_PartyBookingReqVolunteer      |
| clif->pPartyBookingRefuseVolunteer  | clif_parse_PartyBookingRefuseVolunteer   |
| clif->pPartyBookingCancelVolunteer  | clif_parse_PartyBookingCancelVolunteer   |
| clif->pBGQueueRegister              | clif_parse_bgqueue_register              |
| clif->pBGQueueCheckState            | clif_parse_bgqueue_checkstate            |
| clif->pBGQueueRevokeReq             | clif_parse_bgqueue_revoke_req            |
| clif->pBGQueueBattleBeginAck        | clif_parse_bgqueue_battlebegin_ack       |
| clif->pDull                         | clif_parse_dull                          |

### Guild

[Back to Table of Contents](#toc "wikilink")

| Interface Name                 | Function Name                |
|--------------------------------|------------------------------|
| guild->init                   | do_init_guild                 |
| guild->final                  | do_final_guild                |
| guild->skill_get_max          | guild_skill_get_max           |
| guild->checkskill             | guild_checkskill              |
| guild->check_skill_require    | guild_check_skill_require     |
| guild->checkcastles           | guild_checkcastles            |
| guild->isallied               | guild_isallied                |
| guild->search                 | guild_search                  |
| guild->searchname             | guild_searchname              |
| guild->castle_search          | guild_castle_search           |
| guild->mapname2gc             | guild_mapname2gc              |
| guild->mapindex2gc            | guild_mapindex2gc             |
| guild->getavailablesd         | guild_getavailablesd          |
| guild->getindex               | guild_getindex                |
| guild->getposition            | guild_getposition             |
| guild->payexp                 | guild_payexp                  |
| guild->getexp                 | guild_getexp                  |
| guild->create                 | guild_create                  |
| guild->created                | guild_created                 |
| guild->request_info           | guild_request_info            |
| guild->recv_noinfo            | guild_recv_noinfo             |
| guild->recv_info              | guild_recv_info               |
| guild->npc_request_info       | guild_npc_request_info        |
| guild->invite                 | guild_invite                  |
| guild->reply_invite           | guild_reply_invite            |
| guild->member_joined          | guild_member_joined           |
| guild->member_added           | guild_member_added            |
| guild->leave                  | guild_leave                   |
| guild->member_withdraw        | guild_member_withdraw         |
| guild->expulsion              | guild_expulsion               |
| guild->skillup                | guild_skillup                 |
| guild->block_skill            | guild_block_skill             |
| guild->reqalliance            | guild_reqalliance             |
| guild->reply_reqalliance      | guild_reply_reqalliance       |
| guild->allianceack            | guild_allianceack             |
| guild->delalliance            | guild_delalliance             |
| guild->opposition             | guild_opposition              |
| guild->check_alliance         | guild_check_alliance          |
| guild->send_memberinfoshort   | guild_send_memberinfoshort    |
| guild->recv_memberinfoshort   | guild_recv_memberinfoshort    |
| guild->change_memberposition  | guild_change_memberposition   |
| guild->memberposition_changed | guild_memberposition_changed  |
| guild->change_position        | guild_change_position         |
| guild->position_changed       | guild_position_changed        |
| guild->change_notice          | guild_change_notice           |
| guild->notice_changed         | guild_notice_changed          |
| guild->change_emblem          | guild_change_emblem           |
| guild->emblem_changed         | guild_emblem_changed          |
| guild->send_message           | guild_send_message            |
| guild->recv_message           | guild_recv_message            |
| guild->send_dot_remove        | guild_send_dot_remove         |
| guild->skillupack             | guild_skillupack              |
| guild->dobreak                | guild_break                   |
| guild->broken                 | guild_broken                  |
| guild->gm_change              | guild_gm_change               |
| guild->gm_changed             | guild_gm_changed              |
| guild->castle_map_init        | guild_castle_map_init         |
| guild->castledatasave         | guild_castledatasave          |
| guild->castledataloadack      | guild_castledataloadack       |
| guild->castle_reconnect       | guild_castle_reconnect        |
| guild->agit_start             | guild_agit_start              |
| guild->agit_end               | guild_agit_end                |
| guild->agit2_start            | guild_agit2_start             |
| guild->agit2_end              | guild_agit2_end               |
| guild->flag_add               | guild_flag_add                |
| guild->flag_remove            | guild_flag_remove             |
| guild->flags_clear            | guild_flags_clear             |
| guild->aura_refresh           | guild_guildaura_refresh       |

### Homunculus

[Back to Table of Contents](#toc "wikilink")

| Interface Name              | Function Name                  |
|-----------------------------|--------------------------------|
| homun->init                | do_init_homunculus              |
| homun->final               | do_final_homunculus             |
| homun->reload              | homunculus_reload               |
| homun->reload_skill        | homunculus_skill_reload         |
| homun->get_viewdata        | homunculus_get_viewdata         |
| homun->class2type          | homunculus_class2type           |
| homun->damaged             | homunculus_damaged              |
| homun->dead                | homunculus_dead                 |
| homun->vaporize            | homunculus_vaporize             |
| homun->delete              | homunculus_delete               |
| homun->checkskill          | homunculus_checkskill           |
| homun->calc_skilltree      | homunculus_calc_skilltree       |
| homun->skill_tree_get_max  | homunculus_skill_tree_get_max   |
| homun->skillup             | homunculus_skillup              |
| homun->levelup             | homunculus_levelup              |
| homun->change_class        | homunculus_change_class         |
| homun->evolve              | homunculus_evolve               |
| homun->mutate              | homunculus_mutate               |
| homun->gainexp             | homunculus_gainexp              |
| homun->add_intimacy        | homunculus_add_intimacy         |
| homun->consume_intimacy    | homunculus_consume_intimacy     |
| homun->healed              | homunculus_healed               |
| homun->save                | homunculus_save                 |
| homun->menu                | homunculus_menu                 |
| homun->feed                | homunculus_feed                 |
| homun->hunger_timer        | homunculus_hunger_timer         |
| homun->hunger_timer_delete | homunculus_hunger_timer_delete  |
| homun->change_name         | homunculus_change_name          |
| homun->change_name_ack     | homunculus_change_name_ack      |
| homun->db_search           | homunculus_db_search            |
| homun->create              | homunculus_create               |
| homun->init_timers         | homunculus_init_timers          |
| homun->call                | homunculus_call                 |
| homun->recv_data           | homunculus_recv_data            |
| homun->creation_request    | homunculus_creation_request     |
| homun->ressurect           | homunculus_ressurect            |
| homun->revive              | homunculus_revive               |
| homun->stat_reset          | homunculus_stat_reset           |
| homun->shuffle             | homunculus_shuffle              |
| homun->read_db_sub         | homunculus_read_db_sub          |
| homun->read_db             | homunculus_read_db              |
| homun->read_skill_db_sub   | homunculus_read_skill_db_sub    |
| homun->skill_db_read       | homunculus_skill_db_read        |
| homun->exp_db_read         | homunculus_exp_db_read          |

### IRC Bot

[Back to Table of Contents](#toc "wikilink")

| Interface Name          | Function Name      |
|-------------------------|--------------------|
| ircbot->init           | irc_bot_init        |
| ircbot->final          | irc_bot_final       |
| ircbot->parse          | irc_parse           |
| ircbot->parse_sub      | irc_parse_sub       |
| ircbot->parse_source   | irc_parse_source    |
| ircbot->func_search    | irc_func_search     |
| ircbot->connect_timer  | irc_connect_timer   |
| ircbot->identify_timer | irc_identify_timer  |
| ircbot->join_timer     | irc_join_timer      |
| ircbot->send           | irc_send            |
| ircbot->relay          | irc_relay           |
| ircbot->pong           | irc_pong            |
| ircbot->join           | irc_join            |
| ircbot->privmsg        | irc_privmsg         |

### Log

[Back to Table of Contents](#toc "wikilink")

| Interface Name       | Function Name         |
|----------------------|-----------------------|
| logs->pick_pc       | log_pick_pc            |
| logs->pick_mob      | log_pick_mob           |
| logs->zeny          | log_zeny               |
| logs->npc           | log_npc                |
| logs->chat          | log_chat               |
| logs->atcommand     | log_atcommand          |
| logs->branch        | log_branch             |
| logs->mvpdrop       | log_mvpdrop            |
| logs->config_read   | log_config_read        |
| logs->config_done   | log_config_complete    |
| logs->pick_sub      | log_pick_sub_txt       |
| logs->zeny_sub      | log_zeny_sub_txt       |
| logs->npc_sub       | log_npc_sub_txt        |
| logs->chat_sub      | log_chat_sub_txt       |
| logs->atcommand_sub | log_atcommand_sub_txt  |
| logs->branch_sub    | log_branch_sub_txt     |
| logs->mvpdrop_sub   | log_mvpdrop_sub_txt    |

### iMap

[Back to Table of Contents](#toc "wikilink")

| Interface Name                | Function Name              |
|-------------------------------|----------------------------|
| iMap->zone_init              | map_zone_init               |
| iMap->zone_remove            | map_zone_remove             |
| iMap->zone_apply             | map_zone_apply              |
| iMap->zone_change            | map_zone_change             |
| iMap->zone_change2           | map_zone_change2            |
| iMap->getcell                | map_getcell                 |
| iMap->setgatcell             | map_setgatcell              |
| iMap->cellfromcache          | map_cellfromcache           |
| iMap->setusers               | map_setusers                |
| iMap->getusers               | map_getusers                |
| iMap->usercount              | map_usercount               |
| iMap->freeblock              | map_freeblock               |
| iMap->freeblock_lock         | map_freeblock_lock          |
| iMap->freeblock_unlock       | map_freeblock_unlock        |
| iMap->addblock               | map_addblock                |
| iMap->delblock               | map_delblock                |
| iMap->moveblock              | map_moveblock               |
| iMap->count_oncell           | map_count_oncell            |
| iMap->find_skill_unit_oncell | map_find_skill_unit_oncell  |
| iMap->get_new_object_id      | map_get_new_object_id       |
| iMap->search_freecell        | map_search_freecell         |
| iMap->quit                   | map_quit                    |
| iMap->addnpc                 | map_addnpc                  |
| iMap->clearflooritem_timer   | map_clearflooritem_timer    |
| iMap->removemobs_timer       | map_removemobs_timer        |
| iMap->clearflooritem         | map_clearflooritem          |
| iMap->addflooritem           | map_addflooritem            |
| iMap->addnickdb              | map_addnickdb               |
| iMap->delnickdb              | map_delnickdb               |
| iMap->reqnickdb              | map_reqnickdb               |
| iMap->charid2nick            | map_charid2nick             |
| iMap->charid2sd              | map_charid2sd               |
| iMap->id2sd                  | map_id2sd                   |
| iMap->id2md                  | map_id2md                   |
| iMap->id2nd                  | map_id2nd                   |
| iMap->id2hd                  | map_id2hd                   |
| iMap->id2mc                  | map_id2mc                   |
| iMap->id2cd                  | map_id2cd                   |
| iMap->id2bl                  | map_id2bl                   |
| iMap->blid_exists            | map_blid_exists             |
| iMap->mapindex2mapid         | map_mapindex2mapid          |
| iMap->mapname2mapid          | map_mapname2mapid           |
| iMap->mapname2ipport         | map_mapname2ipport          |
| iMap->setipport              | map_setipport               |
| iMap->eraseipport            | map_eraseipport             |
| iMap->eraseallipport         | map_eraseallipport          |
| iMap->addiddb                | map_addiddb                 |
| iMap->deliddb                | map_deliddb                 |
| iMap->nick2sd                | map_nick2sd                 |
| iMap->getmob_boss            | map_getmob_boss             |
| iMap->id2boss                | map_id2boss                 |
| iMap->reloadnpc              | map_reloadnpc               |
| iMap->check_dir              | map_check_dir               |
| iMap->calc_dir               | map_calc_dir                |
| iMap->random_dir             | map_random_dir              |
| iMap->cleanup_sub            | cleanup_sub                 |
| iMap->delmap                 | map_delmap                  |
| iMap->flags_init             | map_flags_init              |
| iMap->iwall_set              | map_iwall_set               |
| iMap->iwall_get              | map_iwall_get               |
| iMap->iwall_remove           | map_iwall_remove            |
| iMap->addmobtolist           | map_addmobtolist            |
| iMap->spawnmobs              | map_spawnmobs               |
| iMap->removemobs             | map_removemobs              |
| iMap->addmap2db              | map_addmap2db               |
| iMap->removemapdb            | map_removemapdb             |
| iMap->clean                  | map_clean                   |
| iMap->do_shutdown            | do_shutdown                 |
| iMap->map_foreachpc          | map_map_foreachpc           |
| iMap->map_foreachmob         | map_map_foreachmob          |
| iMap->map_foreachnpc         | map_map_foreachnpc          |
| iMap->map_foreachregen       | map_map_foreachregen        |
| iMap->map_foreachiddb        | map_map_foreachiddb         |
| iMap->foreachinrange         | map_foreachinrange          |
| iMap->foreachinshootrange    | map_foreachinshootrange     |
| iMap->foreachinarea          | map_foreachinarea           |
| iMap->forcountinrange        | map_forcountinrange         |
| iMap->forcountinarea         | map_forcountinarea          |
| iMap->foreachinmovearea      | map_foreachinmovearea       |
| iMap->foreachincell          | map_foreachincell           |
| iMap->foreachinpath          | map_foreachinpath           |
| iMap->foreachinmap           | map_foreachinmap            |
| iMap->foreachininstance      | map_foreachininstance       |

### Mapit

[Back to Table of Contents](#toc "wikilink")

| Interface Name | Function Name |
|----------------|---------------|
| mapit->alloc  | mapit_alloc    |
| mapit->free   | mapit_free     |
| mapit->first  | mapit_first    |
| mapit->last   | mapit_last     |
| mapit->next   | mapit_next     |
| mapit->prev   | mapit_prev     |
| mapit->exists | mapit_exists   |

### Party

[Back to Table of Contents](#toc "wikilink")

| Interface Name           | Function Name          |
|--------------------------|------------------------|
| party->do_init_party    | do_init_party           |
| party->do_final_party   | do_final_party          |
| party->search           | party_search            |
| party->searchname       | party_searchname        |
| party->getmemberid      | party_getmemberid       |
| party->getavailablesd   | party_getavailablesd    |
| party->create           | party_create            |
| party->created          | party_created           |
| party->request_info     | party_request_info      |
| party->invite           | party_invite            |
| party->member_joined    | party_member_joined     |
| party->member_added     | party_member_added      |
| party->leave            | party_leave             |
| party->removemember     | party_removemember      |
| party->member_withdraw  | party_member_withdraw   |
| party->reply_invite     | party_reply_invite      |
| party->recv_noinfo      | party_recv_noinfo       |
| party->recv_info        | party_recv_info         |
| party->recv_movemap     | party_recv_movemap      |
| party->broken           | party_broken            |
| party->optionchanged    | party_optionchanged     |
| party->changeoption     | party_changeoption      |
| party->changeleader     | party_changeleader      |
| party->send_movemap     | party_send_movemap      |
| party->send_levelup     | party_send_levelup      |
| party->send_logout      | party_send_logout       |
| party->send_message     | party_send_message      |
| party->recv_message     | party_recv_message      |
| party->skill_check      | party_skill_check       |
| party->send_xy_clear    | party_send_xy_clear     |
| party->exp_share        | party_exp_share         |
| party->share_loot       | party_share_loot        |
| party->send_dot_remove  | party_send_dot_remove   |
| party->sub_count        | party_sub_count         |
| party->booking_register | party_booking_register  |
| party->booking_update   | party_booking_update    |
| party->booking_search   | party_booking_search    |
| party->booking_delete   | party_booking_delete    |

### PC

[Back to Table of Contents](#toc "wikilink")

| Interface Name                    | Function Name                   |
|-----------------------------------|---------------------------------|
| pc->class2idx                    | pc_class2idx                     |
| pc->get_group_level              | pc_get_group_level               |
| pc->can_give_items               | pc_can_give_items                |
| pc->can_use_command              | pc_can_use_command               |
| pc->setrestartvalue              | pc_setrestartvalue               |
| pc->makesavestatus               | pc_makesavestatus                |
| pc->respawn                      | pc_respawn                       |
| pc->setnewpc                     | pc_setnewpc                      |
| pc->authok                       | pc_authok                        |
| pc->authfail                     | pc_authfail                      |
| pc->reg_received                 | pc_reg_received                  |
| pc->isequip                      | pc_isequip                       |
| pc->equippoint                   | pc_equippoint                    |
| pc->setinventorydata             | pc_setinventorydata              |
| pc->checkskill                   | pc_checkskill                    |
| pc->checkskill2                  | pc_checkskill2                   |
| pc->checkallowskill              | pc_checkallowskill               |
| pc->checkequip                   | pc_checkequip                    |
| pc->calc_skilltree               | pc_calc_skilltree                |
| pc->calc_skilltree_normalize_job | pc_calc_skilltree_normalize_job  |
| pc->clean_skilltree              | pc_clean_skilltree               |
| pc->setpos                       | pc_setpos                        |
| pc->setsavepoint                 | pc_setsavepoint                  |
| pc->randomwarp                   | pc_randomwarp                    |
| pc->memo                         | pc_memo                          |
| pc->checkadditem                 | pc_checkadditem                  |
| pc->inventoryblank               | pc_inventoryblank                |
| pc->search_inventory             | pc_search_inventory              |
| pc->payzeny                      | pc_payzeny                       |
| pc->additem                      | pc_additem                       |
| pc->getzeny                      | pc_getzeny                       |
| pc->delitem                      | pc_delitem                       |
| pc->paycash                      | pc_paycash                       |
| pc->getcash                      | pc_getcash                       |
| pc->cart_additem                 | pc_cart_additem                  |
| pc->cart_delitem                 | pc_cart_delitem                  |
| pc->putitemtocart                | pc_putitemtocart                 |
| pc->getitemfromcart              | pc_getitemfromcart               |
| pc->cartitem_amount              | pc_cartitem_amount               |
| pc->takeitem                     | pc_takeitem                      |
| pc->dropitem                     | pc_dropitem                      |
| pc->isequipped                   | pc_isequipped                    |
| pc->can_Adopt                    | pc_can_Adopt                     |
| pc->adoption                     | pc_adoption                      |
| pc->updateweightstatus           | pc_updateweightstatus            |
| pc->addautobonus                 | pc_addautobonus                  |
| pc->exeautobonus                 | pc_exeautobonus                  |
| pc->endautobonus                 | pc_endautobonus                  |
| pc->delautobonus                 | pc_delautobonus                  |
| pc->bonus                        | pc_bonus                         |
| pc->bonus2                       | pc_bonus2                        |
| pc->bonus3                       | pc_bonus3                        |
| pc->bonus4                       | pc_bonus4                        |
| pc->bonus5                       | pc_bonus5                        |
| pc->skill                        | pc_skill                         |
| pc->insert_card                  | pc_insert_card                   |
| pc->steal_item                   | pc_steal_item                    |
| pc->steal_coin                   | pc_steal_coin                    |
| pc->modifybuyvalue               | pc_modifybuyvalue                |
| pc->modifysellvalue              | pc_modifysellvalue               |
| pc->follow                       | pc_follow                        |
| pc->stop_following               | pc_stop_following                |
| pc->maxbaselv                    | pc_maxbaselv                     |
| pc->maxjoblv                     | pc_maxjoblv                      |
| pc->checkbaselevelup             | pc_checkbaselevelup              |
| pc->checkjoblevelup              | pc_checkjoblevelup               |
| pc->gainexp                      | pc_gainexp                       |
| pc->nextbaseexp                  | pc_nextbaseexp                   |
| pc->thisbaseexp                  | pc_thisbaseexp                   |
| pc->nextjobexp                   | pc_nextjobexp                    |
| pc->thisjobexp                   | pc_thisjobexp                    |
| pc->gets_status_point            | pc_gets_status_point             |
| pc->need_status_point            | pc_need_status_point             |
| pc->statusup                     | pc_statusup                      |
| pc->statusup2                    | pc_statusup2                     |
| pc->skillup                      | pc_skillup                       |
| pc->allskillup                   | pc_allskillup                    |
| pc->resetlvl                     | pc_resetlvl                      |
| pc->resetstate                   | pc_resetstate                    |
| pc->resetskill                   | pc_resetskill                    |
| pc->resetfeel                    | pc_resetfeel                     |
| pc->resethate                    | pc_resethate                     |
| pc->equipitem                    | pc_equipitem                     |
| pc->unequipitem                  | pc_unequipitem                   |
| pc->checkitem                    | pc_checkitem                     |
| pc->useitem                      | pc_useitem                       |
| pc->skillatk_bonus               | pc_skillatk_bonus                |
| pc->skillheal_bonus              | pc_skillheal_bonus               |
| pc->skillheal2_bonus             | pc_skillheal2_bonus              |
| pc->damage                       | pc_damage                        |
| pc->dead                         | pc_dead                          |
| pc->revive                       | pc_revive                        |
| pc->heal                         | pc_heal                          |
| pc->itemheal                     | pc_itemheal                      |
| pc->percentheal                  | pc_percentheal                   |
| pc->jobchange                    | pc_jobchange                     |
| pc->setoption                    | pc_setoption                     |
| pc->setcart                      | pc_setcart                       |
| pc->setfalcon                    | pc_setfalcon                     |
| pc->setriding                    | pc_setriding                     |
| pc->setmadogear                  | pc_setmadogear                   |
| pc->changelook                   | pc_changelook                    |
| pc->equiplookall                 | pc_equiplookall                  |
| pc->readparam                    | pc_readparam                     |
| pc->setparam                     | pc_setparam                      |
| pc->readreg                      | pc_readreg                       |
| pc->setreg                       | pc_setreg                        |
| pc->readregstr                   | pc_readregstr                    |
| pc->setregstr                    | pc_setregstr                     |
| pc->readregistry                 | pc_readregistry                  |
| pc->setregistry                  | pc_setregistry                   |
| pc->readregistry_str             | pc_readregistry_str              |
| pc->setregistry_str              | pc_setregistry_str               |
| pc->addeventtimer                | pc_addeventtimer                 |
| pc->deleventtimer                | pc_deleventtimer                 |
| pc->cleareventtimer              | pc_cleareventtimer               |
| pc->addeventtimercount           | pc_addeventtimercount            |
| pc->calc_pvprank                 | pc_calc_pvprank                  |
| pc->calc_pvprank_timer           | pc_calc_pvprank_timer            |
| pc->ismarried                    | pc_ismarried                     |
| pc->marriage                     | pc_marriage                      |
| pc->divorce                      | pc_divorce                       |
| pc->get_partner                  | pc_get_partner                   |
| pc->get_father                   | pc_get_father                    |
| pc->get_mother                   | pc_get_mother                    |
| pc->get_child                    | pc_get_child                     |
| pc->bleeding                     | pc_bleeding                      |
| pc->regen                        | pc_regen                         |
| pc->setstand                     | pc_setstand                      |
| pc->candrop                      | pc_candrop                       |
| pc->jobid2mapid                  | pc_jobid2mapid                   |
| pc->mapid2jobid                  | pc_mapid2jobid                   |
| pc->job_name                     | job_name                         |
| pc->setinvincibletimer           | pc_setinvincibletimer            |
| pc->delinvincibletimer           | pc_delinvincibletimer            |
| pc->addspiritball                | pc_addspiritball                 |
| pc->delspiritball                | pc_delspiritball                 |
| pc->addfame                      | pc_addfame                       |
| pc->famerank                     | pc_famerank                      |
| pc->set_hate_mob                 | pc_set_hate_mob                  |
| pc->readdb                       | pc_readdb                        |
| pc->do_init_pc                   | do_init_pc                       |
| pc->do_final_pc                  | do_final_pc                      |
| pc->map_day_timer                | map_day_timer                    |
| pc->map_night_timer              | map_night_timer                  |
| pc->inventory_rentals            | pc_inventory_rentals             |
| pc->inventory_rental_clear       | pc_inventory_rental_clear        |
| pc->inventory_rental_add         | pc_inventory_rental_add          |
| pc->disguise                     | pc_disguise                      |
| pc->isautolooting                | pc_isautolooting                 |
| pc->overheat                     | pc_overheat                      |
| pc->banding                      | pc_banding                       |
| pc->itemcd_do                    | pc_itemcd_do                     |
| pc->load_combo                   | pc_load_combo                    |
| pc->add_talisman                 | pc_add_talisman                  |
| pc->del_talisman                 | pc_del_talisman                  |
| pc->baselevelchanged             | pc_baselevelchanged              |
| pc->level_penalty_mod            | pc_level_penalty_mod             |
| pc->day_timer_tid                | day_timer_tid                    |
| pc->night_timer_tid              | night_timer_tid                  |

### Script

[Back to Table of Contents](#toc "wikilink")

| Interface Name         | Function Name        |
|------------------------|----------------------|
| script->init          | do_init_script        |
| script->final         | do_final_script       |
| script->parse_builtin | script_parse_builtin  |
| script->addScript     | script_hp_add         |
| script->conv_num      | conv_num              |
| script->conv_str      | conv_str              |
| script->rid2sd        | script_rid2sd         |
| script->push_val      | push_val              |
| script->get_val       | get_val               |
| script->get_val2      | get_val2              |
| script->push_str      | push_str              |
| script->push_copy     | push_copy             |
| script->pop_stack     | pop_stack             |
| script->queue         | script_hqueue_get     |
| script->queue_add     | script_hqueue_add     |
| script->queue_del     | script_hqueue_del     |
| script->queue_remove  | script_hqueue_remove  |

### Skill

[Back to Table of Contents](#toc "wikilink")

| Interface Name                         | Function Name                        |
|----------------------------------------|--------------------------------------|
| skill->init                           | do_init_skill                         |
| skill->final                          | do_final_skill                        |
| skill->reload                         | skill_reload                          |
| skill->read_db                        | skill_readdb                          |
| skill->get_index                      | skill_get_index                       |
| skill->get_type                       | skill_get_type                        |
| skill->get_hit                        | skill_get_hit                         |
| skill->get_inf                        | skill_get_inf                         |
| skill->get_ele                        | skill_get_ele                         |
| skill->get_nk                         | skill_get_nk                          |
| skill->get_max                        | skill_get_max                         |
| skill->get_range                      | skill_get_range                       |
| skill->get_range2                     | skill_get_range2                      |
| skill->get_splash                     | skill_get_splash                      |
| skill->get_hp                         | skill_get_hp                          |
| skill->get_mhp                        | skill_get_mhp                         |
| skill->get_sp                         | skill_get_sp                          |
| skill->get_state                      | skill_get_state                       |
| skill->get_zeny                       | skill_get_zeny                        |
| skill->get_num                        | skill_get_num                         |
| skill->get_cast                       | skill_get_cast                        |
| skill->get_delay                      | skill_get_delay                       |
| skill->get_walkdelay                  | skill_get_walkdelay                   |
| skill->get_time                       | skill_get_time                        |
| skill->get_time2                      | skill_get_time2                       |
| skill->get_castnodex                  | skill_get_castnodex                   |
| skill->get_delaynodex                 | skill_get_delaynodex                  |
| skill->get_castdef                    | skill_get_castdef                     |
| skill->get_weapontype                 | skill_get_weapontype                  |
| skill->get_ammotype                   | skill_get_ammotype                    |
| skill->get_ammo_qty                   | skill_get_ammo_qty                    |
| skill->get_unit_id                    | skill_get_unit_id                     |
| skill->get_inf2                       | skill_get_inf2                        |
| skill->get_castcancel                 | skill_get_castcancel                  |
| skill->get_maxcount                   | skill_get_maxcount                    |
| skill->get_blewcount                  | skill_get_blewcount                   |
| skill->get_unit_flag                  | skill_get_unit_flag                   |
| skill->get_unit_target                | skill_get_unit_target                 |
| skill->get_unit_interval              | skill_get_unit_interval               |
| skill->get_unit_bl_target             | skill_get_unit_bl_target              |
| skill->get_spiritball                 | skill_get_spiritball                  |
| skill->get_unit_layout_type           | skill_get_unit_layout_type            |
| skill->get_unit_range                 | skill_get_unit_range                  |
| skill->get_cooldown                   | skill_get_cooldown                    |
| skill->tree_get_max                   | skill_tree_get_max                    |
| skill->get_name                       | skill_get_name                        |
| skill->get_desc                       | skill_get_desc                        |
| skill->chk                            | skill_chk                             |
| skill->get_casttype                   | skill_get_casttype                    |
| skill->get_casttype2                  | skill_get_casttype2                   |
| skill->name2id                        | skill_name2id                         |
| skill->isammotype                     | skill_isammotype                      |
| skill->castend_id                     | skill_castend_id                      |
| skill->castend_pos                    | skill_castend_pos                     |
| skill->castend_map                    | skill_castend_map                     |
| skill->cleartimerskill                | skill_cleartimerskill                 |
| skill->addtimerskill                  | skill_addtimerskill                   |
| skill->additional_effect              | skill_additional_effect               |
| skill->counter_additional_effect      | skill_counter_additional_effect       |
| skill->blown                          | skill_blown                           |
| skill->break_equip                    | skill_break_equip                     |
| skill->strip_equip                    | skill_strip_equip                     |
| skill->id2group                       | skill_id2group                        |
| skill->unitsetting                    | skill_unitsetting                     |
| skill->initunit                       | skill_initunit                        |
| skill->delunit                        | skill_delunit                         |
| skill->init_unitgroup                 | skill_initunitgroup                   |
| skill->del_unitgroup                  | skill_delunitgroup                    |
| skill->clear_unitgroup                | skill_clear_unitgroup                 |
| skill->clear_group                    | skill_clear_group                     |
| skill->unit_onplace                   | skill_unit_onplace                    |
| skill->unit_ondamaged                 | skill_unit_ondamaged                  |
| skill->cast_fix                       | skill_castfix                         |
| skill->cast_fix_sc                    | skill_castfix_sc                      |
| skill->vf_cast_fix                    | skill_vfcastfix                       |
| skill->delay_fix                      | skill_delay_fix                       |
| skill->check_condition_castbegin      | skill_check_condition_castbegin       |
| skill->check_condition_castend        | skill_check_condition_castend         |
| skill->get_requirement                | skill_get_requirement                 |
| skill->check_pc_partner               | skill_check_pc_partner                |
| skill->consume_requirement            | skill_consume_requirement             |
| skill->unit_move                      | skill_unit_move                       |
| skill->unit_move_unit_group           | skill_unit_move_unit_group            |
| skill->unit_onleft                    | skill_unit_onleft                     |
| skill->unit_onout                     | skill_unit_onout                      |
| skill->guildaura_sub                  | skill_guildaura_sub                   |
| skill->sit                            | skill_sit                             |
| skill->brandishspear                  | skill_brandishspear                   |
| skill->repairweapon                   | skill_repairweapon                    |
| skill->identify                       | skill_identify                        |
| skill->weaponrefine                   | skill_weaponrefine                    |
| skill->autospell                      | skill_autospell                       |
| skill->calc_heal                      | skill_calc_heal                       |
| skill->check_cloaking                 | skill_check_cloaking                  |
| skill->enchant_elemental_end          | skill_enchant_elemental_end           |
| skill->not_ok                         | skillnotok                            |
| skill->not_ok_hom                     | skillnotok_hom                        |
| skill->not_ok_mercenary               | skillnotok_mercenary                  |
| skill->chastle_mob_changetarget       | skill_chastle_mob_changetarget        |
| skill->can_produce_mix                | skill_can_produce_mix                 |
| skill->produce_mix                    | skill_produce_mix                     |
| skill->arrow_create                   | skill_arrow_create                    |
| skill->castend_nodamage_id            | skill_castend_nodamage_id             |
| skill->castend_damage_id              | skill_castend_damage_id               |
| skill->castend_pos2                   | skill_castend_pos2                    |
| skill->blockpc_start                  | skill_blockpc_start\_                 |
| skill->blockhomun_start               | skill_blockhomun_start                |
| skill->blockmerc_start                | skill_blockmerc_start                 |
| skill->attack                         | skill_attack                          |
| skill->attack_area                    | skill_attack_area                     |
| skill->area_sub                       | skill_area_sub                        |
| skill->area_sub_count                 | skill_area_sub_count                  |
| skill->check_unit_range               | skill_check_unit_range                |
| skill->check_unit_range_sub           | skill_check_unit_range_sub            |
| skill->check_unit_range2              | skill_check_unit_range2               |
| skill->check_unit_range2_sub          | skill_check_unit_range2_sub           |
| skill->toggle_magicpower              | skill_toggle_magicpower               |
| skill->magic_reflect                  | skill_magic_reflect                   |
| skill->onskillusage                   | skill_onskillusage                    |
| skill->cell_overlap                   | skill_cell_overlap                    |
| skill->timerskill                     | skill_timerskill                      |
| skill->trap_splash                    | skill_trap_splash                     |
| skill->check_condition_mercenary      | skill_check_condition_mercenary       |
| skill->locate_element_field           | skill_locate_element_field            |
| skill->graffitiremover                | skill_graffitiremover                 |
| skill->activate_reverberation         | skill_activate_reverbetion            |
| skill->dance_overlap                  | skill_dance_overlap                   |
| skill->dance_overlap_sub              | skill_dance_overlap_sub               |
| skill->get_unit_layout                | skill_get_unit_layout                 |
| skill->frostjoke_scream               | skill_frostjoke_scream                |
| skill->greed                          | skill_greed                           |
| skill->destroy_trap                   | skill_destroy_trap                    |
| skill->icewall_block                  | skill_icewall_block                   |
| skill->unitgrouptickset_search        | skill_unitgrouptickset_search         |
| skill->dance_switch                   | skill_dance_switch                    |
| skill->check_condition_char_sub       | skill_check_condition_char_sub        |
| skill->check_condition_mob_master_sub | skill_check_condition_mob_master_sub  |
| skill->brandishspear_first            | skill_brandishspear_first             |
| skill->brandishspear_dir              | skill_brandishspear_dir               |
| skill->get_fixed_cast                 | skill_get_fixed_cast                  |
| skill->sit_count                      | skill_sit_count                       |
| skill->sit_in                         | skill_sit_in                          |
| skill->sit_out                        | skill_sit_out                         |
| skill->unitsetmapcell                 | skill_unitsetmapcell                  |
| skill->unit_onplace_timer             | skill_unit_onplace_timer              |
| skill->unit_effect                    | skill_unit_effect                     |
| skill->unit_timer_sub_onplace         | skill_unit_timer_sub_onplace          |
| skill->unit_move_sub                  | skill_unit_move_sub                   |
| skill->blockpc_end                    | skill_blockpc_end                     |
| skill->blockhomun_end                 | skill_blockhomun_end                  |
| skill->blockmerc_end                  | skill_blockmerc_end                   |
| skill->split_atoi                     | skill_split_atoi                      |
| skill->unit_timer                     | skill_unit_timer                      |
| skill->unit_timer_sub                 | skill_unit_timer_sub                  |
| skill->init_unit_layout               | skill_init_unit_layout                |
| skill->parse_row_skilldb              | skill_parse_row_skilldb               |
| skill->parse_row_requiredb            | skill_parse_row_requiredb             |
| skill->parse_row_castdb               | skill_parse_row_castdb                |
| skill->parse_row_castnodexdb          | skill_parse_row_castnodexdb           |
| skill->parse_row_unitdb               | skill_parse_row_unitdb                |
| skill->parse_row_producedb            | skill_parse_row_producedb             |
| skill->parse_row_createarrowdb        | skill_parse_row_createarrowdb         |
| skill->parse_row_abradb               | skill_parse_row_abradb                |
| skill->parse_row_spellbookdb          | skill_parse_row_spellbookdb           |
| skill->parse_row_magicmushroomdb      | skill_parse_row_magicmushroomdb       |
| skill->parse_row_reproducedb          | skill_parse_row_reproducedb           |
| skill->parse_row_improvisedb          | skill_parse_row_improvisedb           |
| skill->parse_row_changematerialdb     | skill_parse_row_changematerialdb      |
| skill->usave_add                      | skill_usave_add                       |
| skill->usave_trigger                  | skill_usave_trigger                   |
| skill->cooldown_load                  | skill_cooldown_load                   |
| skill->spellbook                      | skill_spellbook                       |
| skill->block_check                    | skill_block_check                     |
| skill->detonator                      | skill_detonator                       |
| skill->check_camouflage               | skill_check_camouflage                |
| skill->magicdecoy                     | skill_magicdecoy                      |
| skill->poisoningweapon                | skill_poisoningweapon                 |
| skill->select_menu                    | skill_select_menu                     |
| skill->elementalanalysis              | skill_elementalanalysis               |
| skill->changematerial                 | skill_changematerial                  |
| skill->get_elemental_type             | skill_get_elemental_type              |

### Vending

[Back to Table of Contents](#toc "wikilink")

| Interface Name      | Function Name          |
|---------------------|------------------------|
| vending->init      | init                    |
| vending->final     | final                   |
| vending->close     | vending_closevending    |
| vending->open      | vending_openvending     |
| vending->list      | vending_vendinglistreq  |
| vending->purchase  | vending_purchasereq     |
| vending->search    | vending_search          |
| vending->searchall | vending_searchall       |
