import re
from utility.data_handler import read_json, get_data_path
import pandas as pd
import json

sextant_list = [
    [
        "Awakened Sextant",
        1,
        "Your Maps are Alluring3 uses remaining ",
        "default 10"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 25 additional Clusters of Mysterious Barrels3 uses remainingmap bonus barrel % [10] ",
        "default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 35 additional Clusters of Mysterious Barrels15 uses remainingmap bonus barrel % [10] ",
        "default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Maps found in your Maps are Corrupted with 8 Modifiers3 uses remaining ",
        "default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Maps found in your Maps are Corrupted with 8 Modifiers15 uses remaining ",
        "default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional Winged ScarabYour Maps contain an additional Tormented Betrayer15 uses remainingmap extra content weighting [1] ",
        "default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional Gilded ScarabYour Maps contain an additional Tormented Betrayer3 uses remainingmap extra content weighting [1] ",
        "default 60"
    ],
    [
        "Awakened Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional Polished ScarabYour Maps contain an additional Tormented Betrayer3 uses remainingmap extra content weighting [1] ",
        "default 175"
    ],
    [
        "Awakened Sextant",
        1,
        "Items found in your Identified Maps are Identified20% increased Pack Size in your Unidentified Maps3 uses remaining ",
        "default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Items found in your Identified Maps are Identified25% increased Pack Size in your Unidentified Maps15 uses remaining ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 25 additional Clusters of Mysterious Barrels3 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 35 additional Clusters of Mysterious Barrels15 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 25 additional Clusters of Mysterious Barrels3 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 35 additional Clusters of Mysterious Barrels15 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 25 additional Clusters of Mysterious Barrels3 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 35 additional Clusters of Mysterious Barrels15 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 25 additional Clusters of Mysterious Barrels3 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 35 additional Clusters of Mysterious Barrels15 uses remainingmap bonus barrel % [10] ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional MapYour Maps contain an additional Tormented Heretic3 uses remainingmap extra content weighting [1] ",
        "default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional MapYour Maps contain an additional Tormented Heretic15 uses remainingmap extra content weighting [1] ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional Unique ItemYour Maps contain an additional Tormented Graverobber3 uses remainingmap extra content weighting [1] ",
        "default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses deal 20% increased DamageYour Maps have 20% Quality3 uses remaining ",
        "default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses have 20% increased LifeQuality bonus of your Maps also applies to Rarity of Items found3 uses remaining ",
        "default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses of your Corrupted Maps drop 2 additional Vaal ItemsItems found in your Maps have 5% chance to be Corrupted3 uses remaining ",
        "default 500"
    ],
    [
        "Elevated Sextant",
        1,
        "Map Bosses of your Corrupted Maps drop 3 additional Vaal ItemsItems found in your Maps have 5% chance to be Corrupted15 uses remaining ",
        "default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "The First 3 Possessed Monsters drop an additional Rusted ScarabYour Maps contain an additional Tormented Betrayer3 uses remainingmap extra content weighting [1] ",
        "default 520"
    ],
    [
        "Awakened Sextant",
        1,
        "Players and their Minions cannot take Reflected DamageYour Maps contain 4 additional Packs with Mirrored Rare Monsters3 uses remaining ",
        "default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Players and their Minions cannot take Reflected DamageYour Maps contain 5 additional Packs with Mirrored Rare Monsters15 uses remaining ",
        "default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Player's Life and Mana Recovery from Flasks are instantYour Maps contain 6 additional packs of Monsters that Heal3 uses remaining ",
        "default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Player's Life and Mana Recovery from Flasks are instantYour Maps contain 8 additional packs of Monsters that Heal15 uses remaining ",
        "default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Strongbox Monsters are EnragedStrongbox Monsters have 500% increased Item QuantityYour Maps contain an additional Strongbox3 uses remainingmap extra content weighting [0]map strongbox monsters movement velocity +% [25] ",
        "hall_of_grandmasters 0no_strongboxes 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Strongbox Monsters are EnragedStrongbox Monsters have 600% increased Item QuantityYour Maps contain an additional Strongbox15 uses remainingmap extra content weighting [0]map strongbox monsters movement velocity +% [30] ",
        "hall_of_grandmasters 0no_strongboxes 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses deal 100% more DamageMap Bosses have 200% more LifeFinal Map Boss in each Map drops an additional Shaper Guardian Map (Tier 14+)3 uses remaining ",
        "no_boss 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Map Bosses deal 100% more DamageMap Bosses have 200% more LifeFinal Map Boss in each Map drops an additional Shaper Guardian Map (Tier 14+)15 uses remaining ",
        "no_boss 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses deal 100% more DamageMap Bosses have 200% more LifeFinal Map Boss in each Map drops an additional Elder Guardian Map (Tier 14+)3 uses remaining ",
        "no_boss 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Map Bosses deal 100% more DamageMap Bosses have 200% more LifeFinal Map Boss in each Map drops an additional Elder Guardian Map (Tier 14+)15 uses remaining ",
        "no_boss 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses deal 100% more DamageMap Bosses have 200% more LifeFinal Map Boss in each Map drops an additional Conqueror Map3 uses remaining ",
        "no_boss 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Map Bosses deal 100% more DamageMap Bosses have 200% more LifeFinal Map Boss in each Map drops an additional Conqueror Map15 uses remaining ",
        "no_boss 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses are accompanied by BodyguardsAn additional Map drops on Completing your Maps3 uses remaining ",
        "no_boss 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Map Bosses are accompanied by Bodyguards2 additional Maps drop on Completing your Maps15 uses remaining ",
        "no_boss 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses are accompanied by a mysterious HarbingerMap Bosses drop additional Currency ShardsHarbingers in your Maps drop additional Currency Shards3 uses remainingmap extra content weighting [1] ",
        "no_boss 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Map Bosses are accompanied by a mysterious HarbingerMap Bosses drop additional Currency ShardsHarbingers in your Maps drop additional Currency Shards15 uses remainingmap extra content weighting [1] ",
        "no_boss 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Map Bosses drop 1 additional Unique Item3 uses remaining ",
        "no_boss 0default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain hunted traitors3 uses remaining ",
        "no_monster_packs 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain hunted traitors15 uses remaining ",
        "no_monster_packs 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 6 additional packs of Corrupted Vaal MonstersItems dropped by Corrupted Vaal Monsters in your Maps have 25% chance to be Corrupted3 uses remaining ",
        "no_monster_packs 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 8 additional packs of Corrupted Vaal MonstersItems dropped by Corrupted Vaal Monsters in your Maps have 30% chance to be Corrupted15 uses remaining ",
        "no_monster_packs 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 6 additional packs of Corrupted Vaal MonstersYour Maps have a 50% chance to contain Gifts of the Red Queen per Mortal Fragment usedYour Maps have a 50% chance to contain Gifts of the Sacrificed per Sacrifice Fragment used3 uses remainingmap extra content weighting [1] ",
        "no_monster_packs 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 8 additional packs of Corrupted Vaal MonstersYour Maps have a 50% chance to contain Gifts of the Red Queen per Mortal Fragment usedYour Maps have a 50% chance to contain Gifts of the Sacrificed per Sacrifice Fragment used15 uses remainingmap extra content weighting [1] ",
        "no_monster_packs 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Players' Vaal Skills do not apply Soul Gain PreventionYour Maps contain 6 additional packs of Corrupted Vaal Monsters3 uses remaining ",
        "no_monster_packs 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Players' Vaal Skills do not apply Soul Gain PreventionYour Maps contain 8 additional packs of Corrupted Vaal Monsters15 uses remaining ",
        "no_monster_packs 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "25% increased Magic Pack Size3 uses remaining ",
        "no_monster_packs 0default 500"
    ],
    [
        "Elevated Sextant",
        1,
        "30% increased Magic Pack Size15 uses remaining ",
        "no_monster_packs 0default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Rogue Exiles deal 20% increased DamageRogue Exiles drop 2 additional JewelsRogue Exiles in your Maps have 20% increased LifeYour Maps are inhabited by 2 additional Rogue Exiles3 uses remainingmap extra content weighting [0] ",
        "no_monster_packs 0default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Players gain an additional Vaal Soul on KillYour Maps contain 6 additional packs of Corrupted Vaal Monsters3 uses remaining ",
        "no_monster_packs 0default 500"
    ],
    [
        "Elevated Sextant",
        1,
        "Players gain an additional Vaal Soul on KillYour Maps contain 8 additional packs of Corrupted Vaal Monsters15 uses remaining ",
        "no_monster_packs 0default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Players and Monsters take 12% increased Fire DamageYour Maps contain 6 additional packs of Monsters that deal Fire Damage3 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Players and Monsters take 14% increased Fire DamageYour Maps contain 8 additional packs of Monsters that deal Fire Damage15 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Players and Monsters take 12% increased Cold DamageYour Maps contain 6 additional packs of Monsters that deal Cold Damage3 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Players and Monsters take 14% increased Cold DamageYour Maps contain 8 additional packs of Monsters that deal Cold Damage15 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Players and Monsters take 12% increased Lightning DamageYour Maps contain 6 additional packs of Monsters that deal Lightning Damage3 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Players and Monsters take 14% increased Lightning DamageYour Maps contain 8 additional packs of Monsters that deal Lightning Damage15 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Players and Monsters take 12% increased Physical DamageYour Maps contain 6 additional packs of Monsters that deal Physical Damage3 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Players and Monsters take 14% increased Physical DamageYour Maps contain 8 additional packs of Monsters that deal Physical Damage15 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Players and Monsters take 12% increased Chaos DamageYour Maps contain 6 additional packs of Monsters that deal Chaos Damage3 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Players and Monsters take 14% increased Chaos DamageYour Maps contain 8 additional packs of Monsters that deal Chaos Damage15 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 6 additional packs of Monsters that Convert when Killed3 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 8 additional packs of Monsters that Convert when Killed15 uses remaining ",
        "no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain a Mirror of Delirium3 uses remainingmap affliction league [1] ",
        "no_monster_packs 0unique_map 0default 100"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain a Mirror of Delirium15 uses remainingmap affliction league [1] ",
        "no_monster_packs 0unique_map 0default 100"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain The Sacred Grove3 uses remainingmap extra content weighting [1]map harvest league [1] ",
        "no_monster_packs 0unique_map 0default 100"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain The Sacred Grove15 uses remainingmap extra content weighting [1]map harvest league [1] ",
        "no_monster_packs 0unique_map 0default 100"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain Ritual Altars3 uses remaining ",
        "no_monster_packs 0unique_map 0default 100"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain Ritual Altars15 uses remaining ",
        "no_monster_packs 0unique_map 0default 100"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain an additional Legion Encounter3 uses remainingmap extra content weighting [1]map legion league [1] ",
        "no_monster_packs 0unique_map 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain an additional Legion Encounter15 uses remainingmap extra content weighting [1]map legion league [1] ",
        "no_monster_packs 0unique_map 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Area contains Metamorph Monsters3 uses remainingmap extra content weighting [1] ",
        "no_monster_packs 0unique_map 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Area contains Metamorph Monsters15 uses remainingmap extra content weighting [1] ",
        "no_monster_packs 0unique_map 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Area contains a Smuggler's Cache3 uses remaining ",
        "no_monster_packs 0unique_map 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Area contains a Smuggler's Cache15 uses remaining ",
        "no_monster_packs 0unique_map 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain a Blight Encounter3 uses remainingmap blight league [1]map extra content weighting [1] ",
        "no_monster_packs 0unique_map 0map_has_blight_encounter 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain a Blight Encounter15 uses remainingmap blight league [1]map extra content weighting [1] ",
        "no_monster_packs 0unique_map 0map_has_blight_encounter 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 2 additional StrongboxesStrongboxes in your Maps are CorruptedStrongboxes in your Maps are at least Rare3 uses remainingmap extra content weighting [1] ",
        "no_strongboxes 0default 500"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 3 additional StrongboxesStrongboxes in your Maps are CorruptedStrongboxes in your Maps are at least Rare15 uses remainingmap extra content weighting [1] ",
        "no_strongboxes 0default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Breaches in your Maps belong to XophBreaches in your Maps contain 3 additional Clasped Hands3 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Breaches in your Maps belong to XophBreaches in your Maps contain 3 additional Clasped Hands15 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Breaches in your Maps belong to TulBreaches in your Maps contain 3 additional Clasped Hands3 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Breaches in your Maps belong to TulBreaches in your Maps contain 3 additional Clasped Hands15 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Breaches in your Maps belong to EshBreaches in your Maps contain 3 additional Clasped Hands3 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Breaches in your Maps belong to EshBreaches in your Maps contain 3 additional Clasped Hands15 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Breaches in your Maps belong to Uul-NetolBreaches in your Maps contain 3 additional Clasped Hands3 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Breaches in your Maps belong to Uul-NetolBreaches in your Maps contain 3 additional Clasped Hands15 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Breaches in your Maps belong to ChayulaBreaches in your Maps contain 3 additional Clasped Hands3 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Breaches in your Maps belong to ChayulaBreaches in your Maps contain 3 additional Clasped Hands15 uses remaining ",
        "unique_map 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps can contain BreachesYour Maps contain an additional Breach3 uses remainingmap extra content weighting [1] ",
        "unique_map 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps can contain BreachesYour Maps contain 2 additional Breaches15 uses remainingmap extra content weighting [1] ",
        "unique_map 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain an additional AbyssYour Maps can contain Abysses3 uses remainingmap extra content weighting [1] ",
        "unique_map 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 2 additional AbyssesYour Maps can contain Abysses15 uses remainingmap extra content weighting [1] ",
        "unique_map 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Slaying Enemies close together can attract monsters from Beyond this realm25% increased Beyond Demon Pack Size in your Maps3 uses remainingmap extra content weighting [1] ",
        "unique_map 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Slaying Enemies close together can attract monsters from Beyond this realm35% increased Beyond Demon Pack Size in your Maps15 uses remainingmap extra content weighting [1] ",
        "unique_map 0default 250"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain Einhar3 uses remainingmap extra content weighting [1]map mission id [2] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain Einhar15 uses remainingmap extra content weighting [1]map mission id [2] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain Alva3 uses remainingmap extra content weighting [1]map mission id [3] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain Alva15 uses remainingmap extra content weighting [1]map mission id [3] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain Niko3 uses remainingmap extra content weighting [1]map mission id [5] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain Niko15 uses remainingmap extra content weighting [1]map mission id [5] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain Jun3 uses remainingmap extra content weighting [1]map mission id [6] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain Jun15 uses remainingmap extra content weighting [1]map mission id [6] ",
        "unique_map 0elder_occupied_map 0has_atlas_mission 0default 125"
    ],
    [
        "Awakened Sextant",
        1,
        "Create a copy of Beasts Captured in your Maps3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Create a copy of Beasts Captured in your Maps15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain 100% increased number of Runic Monster Markers3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain 100% increased number of Runic Monster Markers15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Legion Monsters in your Maps have 100% more LifeSplinters and Emblems dropped by Legion Monsters in your Maps are duplicated3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Legion Monsters in your Maps have 100% more LifeSplinters and Emblems dropped by Legion Monsters in your Maps are duplicated15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Catalysts dropped by Metamorphs in your Maps are DuplicatedMetamorphs in your Maps have 100% more Life3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Catalysts dropped by Metamorphs in your Maps are DuplicatedMetamorphs in your Maps have 100% more Life15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Oils found in your Maps are 1 tier higherCost of Building and Upgrading Blight Towers in your Maps is doubled3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Oils found in your Maps are 1 tier higherCost of Building and Upgrading Blight Towers in your Maps is doubled15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "100% increased Intelligence gained from Immortal Syndicate targets encountered in your Maps3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "100% increased Intelligence gained from Immortal Syndicate targets encountered in your Maps15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Delirium Reward Bars fill 100% faster in your Maps3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Delirium Reward Bars fill 100% faster in your Maps15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Lifeforce dropped by Harvest Monsters in your Maps is DuplicatedHarvest Monsters in your Maps have 100% more LifeHarvests in your Maps contain at least one Crop of Blue Plants3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Lifeforce dropped by Harvest Monsters in your Maps is DuplicatedHarvest Monsters in your Maps have 100% more LifeHarvests in your Maps contain at least one Crop of Purple Plants3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Lifeforce dropped by Harvest Monsters in your Maps is DuplicatedHarvest Monsters in your Maps have 100% more LifeHarvests in your Maps contain at least one Crop of Yellow Plants3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Lifeforce dropped by Harvest Monsters in your Maps is DuplicatedHarvest Monsters in your Maps have 100% more LifeHarvests in your Maps contain at least one Crop of Blue Plants15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Lifeforce dropped by Harvest Monsters in your Maps is DuplicatedHarvest Monsters in your Maps have 100% more LifeHarvests in your Maps contain at least one Crop of Purple Plants15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Lifeforce dropped by Harvest Monsters in your Maps is DuplicatedHarvest Monsters in your Maps have 100% more LifeHarvests in your Maps contain at least one Crop of Yellow Plants15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Non-Unique Heist Contracts found in your Maps have an additional Implicit Modifier3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Non-Unique Heist Contracts found in your Maps have an additional Implicit Modifier15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Rerolling Favours at Ritual Altars in your Maps has no Cost the first 1 time3 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Elevated Sextant",
        1,
        "Rerolling Favours at Ritual Altars in your Maps has no Cost the first 1 time15 uses remaining ",
        "unique_map 0no_monster_packs 0default 50"
    ],
    [
        "Awakened Sextant",
        1,
        "Monsters Imprisoned by Essences have a 50% chance to contain a Remnant of CorruptionYour Maps contain an additional Essence3 uses remainingmap extra content weighting [1] ",
        "unique_map 0no_monster_packs 0default 500"
    ],
    [
        "Elevated Sextant",
        1,
        "Monsters Imprisoned by Essences have a 50% chance to contain a Remnant of CorruptionYour Maps contain 2 additional Essences15 uses remainingmap extra content weighting [1] ",
        "unique_map 0no_monster_packs 0default 500"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Magic Maps contain 4 additional packs of Magic MonstersYour Normal Maps contain 4 additional packs of Normal MonstersYour Rare Maps contain 4 additional Rare Monster packs3 uses remaining ",
        "unique_map 0no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Magic Maps contain 5 additional packs of Magic MonstersYour Normal Maps contain 5 additional packs of Normal MonstersYour Rare Maps contain 5 additional Rare Monster packs15 uses remaining ",
        "unique_map 0no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain an additional Gloom Shrine50% increased Duration of Shrine Effects on Players in your Maps3 uses remainingmap extra content weighting [1] ",
        "unique_map 0no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain an additional Gloom ShrineYour Maps contain an additional Shrine50% increased Duration of Shrine Effects on Players in your Maps15 uses remainingmap extra content weighting [1] ",
        "unique_map 0no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Your Maps contain an additional Resonating Shrine50% increased Duration of Shrine Effects on Players in your Maps3 uses remainingmap extra content weighting [1] ",
        "unique_map 0no_monster_packs 0default 1000"
    ],
    [
        "Elevated Sextant",
        1,
        "Your Maps contain an additional Resonating ShrineYour Maps contain an additional Shrine50% increased Duration of Shrine Effects on Players in your Maps15 uses remainingmap extra content weighting [1] ",
        "unique_map 0no_monster_packs 0default 1000"
    ],
    [
        "Awakened Sextant",
        1,
        "Unique Monsters drop Corrupted Items3 uses remaining ",
        "vaults_of_atziri 0hall_of_grandmasters 0default 250"
    ],
    [
        "Elevated Sextant",
        1,
        "Unique Monsters drop Corrupted Items15 uses remaining ",
        "vaults_of_atziri 0hall_of_grandmasters 0default 250"
    ]
]

item = []
level = []
descriptions = []
descriptions_sorted = []

weightings = []
weightings_sorted = []


# separate entries
for sextant in sextant_list:
    item.append(sextant[0])
    level.append(sextant[1])
    descriptions.append(sextant[2])
    weightings.append(sextant[3])


# work on weightings (easier)
pattern_weights = r"(\w_*\w+\s\d+)"
# should work but proof!
for i, weight in enumerate(weightings):
    default = -1
    elder = -1
    atlas = -1
    hall = -1
    strongbox = -1
    unique = -1
    monster = -1
    boss = -1
    blight = -1
    vaults = -1

    # result = regex_weightings.findall(weight)
    result = re.findall(pattern_weights, weight)

    for entry in result:
        splited = entry.split()
        if splited[0] == "default":
            default = splited[-1]
        if splited[0] == "elder_occupied_map":
            elder = splited[-1]
        if splited[0] == "has_atlas_mission":
            atlas = splited[-1]
        if splited[0] == "hall_of_grandmasters":
            hall = splited[-1]
        if splited[0] == "no_strongboxes":
            strongbox = splited[-1]
        if splited[0] == "unique_map":
            unique = splited[-1]
        if splited[0] == "no_monster_packs":
            monster = splited[-1]
        if splited[0] == "no_boss":
            boss = splited[-1]
        if splited[0] == "map_has_blight_encounter":
            blight = splited[-1]
        if splited[0] == "vaults_of_atziri":
            vaults = splited[-1]


    result_list = {
        "default": default,
        "elder_occupied_map": elder,
        "has_atlas_mission": atlas,
        "hall_of_grandmasters": hall,
        "no_strongboxes": strongbox,
        "unique_map": unique,
        "no_monster_packs": monster,
        "no_boss": boss,
        "map_has_blight_encounter": blight,
        "vaults_of_atziri": vaults
    }
    weightings_sorted.append(result_list)

pattern_description = ""