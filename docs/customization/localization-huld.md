# Localization / Translations (HULD)

Hercules servers are able to provide some sort of multi-language thanks to a feature 
called Hercules Ultimate Localization Design (HULD for short).


## How it works

Translations are stored in PO files, a standard format for translations. Those files
are stored in Hercules and follow a structure that imitates the NPC folder (plus
a few other files).

During startup, Hercules loads those files as additional languages and whenever
a NPC message is displayed, the player's current language is used.

A default language is set in the configs, and additional languages may be selected
by each player by using the `@lang` command.


## Generating translation files

In order to start translating the NPCs and other translatable messages, you must
first generate the translation files.

To do that:

1. Build your server, including HPM Hook plugins
2. Build the `generate-translations.c` plugin (see [HPM](./hercules-plugin-manager.md))
3. Run `./map-server --load-plugin HPMHooking --load-plugin generate-translations --generate-translations` this will:
   1. Start map-server with "HPM Hooking" and "generate-translations" plugins loaded
   2. Ask map-server to actually generate the translation files
4. Once it complete, map-server will automatically shut down, this is expected.
5. You can now see a folder called `generated_translations` in your repository root
6. This folder contains everything you need to translate, see [Adding a language](#adding-a-language)


## Adding a language

Once you have the translation files folder (either downloaded from somewhere or generated with [Generating translations](#generating-translation-files)),
you need to add the folder path to `db/translations.conf`.

For example, if you have the `Spanish` language files at `db/Spanish/`, your
`db/translations.conf` should look like this:

```
translations: (
	"db/Spanish",
)
```

From now on, `@lang Spanish` will give a player the Spanish translation.


## Default language

The server's default language is defined in `conf/map/map-server.conf`:

```
	// When employing more than one language (see db/translations.conf),
	// this setting is used as a fallback
	default_language: "English"
```

Following the example above, you could change the value here to `Spanish` for players
to start their characters having the Spanish translation. (They could switch later on)


## Translatable strings

By default, Hercules will pick every string used in `mes`, `mesf` and `select` commands,
but you can explicitily tell Hercules that strings in other parts of your script
must also be translated by using the `_()` macro.

For example:

```HercScript
.@status1$ = "Closed"; // This won't be translated
.@status2$ = _("Available"); // This will be translated
```


## Caveats

### Global messages

Messages sent to many players at once, like broadcasts will use the attached player
language.

This is for performance reasons, since sending messages in each player language
would require building separate packets/messages for each player (or group of players).


### "Unattached" messages

When a message is sent by a script that doesn't have a player attached,
the message will be sent in the server's default language.

This is for performance reasons, since sending messages in the default language
would require building separate packets/messages for each player (or group of players).
Additionally, since no player is attached, there is no player language to use.

```HercScript
prontera,150,150,0	script	test huld	4_F_SISTER,{
	mes("Text with player attached. In player language");
	announce(_("Text in player language for everyone."), bc_all);
	initnpctimer();
	close();

OnTimer1500:
	// Player is not attached here.
	npctalk("Hi, i'm talking in server default language.");
	end;
}

```


### Player gender

There is no way to have variation by player gender for the same message.

One strategy to work around that is to include a space at the end of the message
for one of the genders, for example:

```HercScript
if (Sex == SEX_MALE) {
	mes("Hello");
} else {
	mes("Hello ");
}

```

This would generate 2 messages for translation.
