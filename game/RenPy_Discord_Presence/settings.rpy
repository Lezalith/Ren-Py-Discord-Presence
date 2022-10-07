# Ran before discord_rich_presence present on -950.
init offset = -960

# Application Id - This is gotten from Discord's Developer Portal. 
# Process of setting it up is described on GitHub under the Wiki tab, or locally in [TO-BE-WRITTEN].md
define discord.application_id = "1020817080838262795"

#####################################################################################################################################

# State of the Presence upon the game's launch.
# In the preview project, it is overwritten in script.rpy to refer one of the two defined examples.
define discord.main_menu_state = { "details" : "In the Main Menu.",
                                       "large_image" : "lezalith"}

# State of the Presence when the game is started.
define discord.start_state = { "details" : "Reading the Story.",
                                       "large_image" : "lezalith"}

# Name of the label that should update Presence to`start_state` when entered.
# Can also be a list label names, if you have multiple start labels. 
define discord.start_label = "functionality_example"

# The state is basically a Dict with all the properties of the presence state displayed when the game is launched.
# keys correspond not to Presence Fields, but to pypresence arguments! 
# They are all well described in Readme, but here is a cheat sheet from pypresence documentation:
#
# state (str) – the user’s current status
# details (str) – what the player is currently doing
# start (int) – epoch time for game start
# end (int) – epoch time for game end
# large_image (str) – name of the uploaded image for the large profile artwork
# large_text (str) – tooltip for the large image
# small_image (str) – name of the uploaded image for the small profile artwork
# small_text (str) – tootltip for the small image
# party_size (list) – current size of the player’s party, lobby, or group, and the max in this format: [1,4]
# buttons (list) – list of up to two dicts for buttons, in the format {"label": "My Website", "url": "https://qtqt.cf"}
# 
# time (bool) is a special non-pypresence property. Giving it the True value displays the Elapsed Time in the presence (default), False hides it.

#####################################################################################################################################

# These variables control the print functions across this script. They work if True, they're ignored if False.
# Prints are shown inside game's console (if turned on) and in the game's log.txt file.
define discord.log_important = True # Shows whether the Presence was initialized and closed correctly.
define discord.log_properties = True # Records properties whenever they change with set or update methods.
define discord.log_restore = True # Notes whenever the properties get rolled back or loaded from a save file, and what they were restored into.