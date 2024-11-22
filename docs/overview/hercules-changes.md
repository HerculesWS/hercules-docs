!!! warning
	This page may contain outdated information, incompatible with the current version of Hercules and its coding standards.


A Compilation of noteworthy changes done by Hercules throughout its existence, noteworthy being considered new features,
modifications to existent features (e.g. script command) among other things.

# 2013

## January

## February

## March

## April

## May

### Instances / Instancing

Since May 30th on the [Slasher Patch](https://herc.ws/board/topic/928-memory-slasher-may-30-patch/%7CMemory)

#### Functionality/Feature

- map server was made capable of creating instances of any maps regardless of client-side edits, e.g. one can clone
  prontera and call it "mymapname"
- instances were modified to be employed in 4 distinct ways:
  - by nobody (server type instance, to be used with special map names)
  - by a sole character
  - by a party
  - by by a guild

#### Script Command Changes

- `instance_create` 2nd param was renamed to owner_id, (was party_id) , and it got a 3rd
  optional param that defines what kind of owner id it is (when not provided, assumes party_id, for backwards
  compatibility), available options are (`IOT_` stands for INSTANCE OWNER TYPE) IOT_NONE (0), IOT_CHAR (1), IOT_PARTY (2)
  and IOT_GUILD (3).
- `instance_destroy` no longer autodetects instance id from party id
- `instance_attachmap` was given a 4th, optional, param, `"<new map name>"`, it allows a
  entirely new map name to be specified for the instance (without the need of client-side edits). this option can be
  best employed when used on a instance of `<owner_type>` IOT_NONE
- `instance_detachmap` no longer autodetects instance id from party id
- `instance_id` no longer supports any param
- `instance_set_timeout` no longer autodetects instance id from party id
- `instance_announce` no longer autodetects instance id from party id, and to tell it to
  autodetect from the attached script you must set instance_id param as -1 as opposed to 0
- `instance_npcname` no longer autodetects instance id from party id
- `has_instance` no longer autodetects instance from party, however it now checks if attached
  player possesses a instance with same map as `has_instance(<param>)` checks for
- `instance_warpall` no longer autodetects instance from party

#### Other Changes

- instance IDs (valid ones) are now always >= 0 as opposed to > 0

## June

## July
