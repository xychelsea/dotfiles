"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import sys
import typing

import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ActionResult:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ActionResultEnumTypeWrapper(
    google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ActionResult.ValueType], builtins.type
):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Success: _ActionResult.ValueType  # 1
    NotSupported: _ActionResult.ValueType  # 2
    Error: _ActionResult.ValueType  # 3
    CantQueueThatOrder: _ActionResult.ValueType  # 4
    Retry: _ActionResult.ValueType  # 5
    Cooldown: _ActionResult.ValueType  # 6
    QueueIsFull: _ActionResult.ValueType  # 7
    RallyQueueIsFull: _ActionResult.ValueType  # 8
    NotEnoughMinerals: _ActionResult.ValueType  # 9
    NotEnoughVespene: _ActionResult.ValueType  # 10
    NotEnoughTerrazine: _ActionResult.ValueType  # 11
    NotEnoughCustom: _ActionResult.ValueType  # 12
    NotEnoughFood: _ActionResult.ValueType  # 13
    FoodUsageImpossible: _ActionResult.ValueType  # 14
    NotEnoughLife: _ActionResult.ValueType  # 15
    NotEnoughShields: _ActionResult.ValueType  # 16
    NotEnoughEnergy: _ActionResult.ValueType  # 17
    LifeSuppressed: _ActionResult.ValueType  # 18
    ShieldsSuppressed: _ActionResult.ValueType  # 19
    EnergySuppressed: _ActionResult.ValueType  # 20
    NotEnoughCharges: _ActionResult.ValueType  # 21
    CantAddMoreCharges: _ActionResult.ValueType  # 22
    TooMuchMinerals: _ActionResult.ValueType  # 23
    TooMuchVespene: _ActionResult.ValueType  # 24
    TooMuchTerrazine: _ActionResult.ValueType  # 25
    TooMuchCustom: _ActionResult.ValueType  # 26
    TooMuchFood: _ActionResult.ValueType  # 27
    TooMuchLife: _ActionResult.ValueType  # 28
    TooMuchShields: _ActionResult.ValueType  # 29
    TooMuchEnergy: _ActionResult.ValueType  # 30
    MustTargetUnitWithLife: _ActionResult.ValueType  # 31
    MustTargetUnitWithShields: _ActionResult.ValueType  # 32
    MustTargetUnitWithEnergy: _ActionResult.ValueType  # 33
    CantTrade: _ActionResult.ValueType  # 34
    CantSpend: _ActionResult.ValueType  # 35
    CantTargetThatUnit: _ActionResult.ValueType  # 36
    CouldntAllocateUnit: _ActionResult.ValueType  # 37
    UnitCantMove: _ActionResult.ValueType  # 38
    TransportIsHoldingPosition: _ActionResult.ValueType  # 39
    BuildTechRequirementsNotMet: _ActionResult.ValueType  # 40
    CantFindPlacementLocation: _ActionResult.ValueType  # 41
    CantBuildOnThat: _ActionResult.ValueType  # 42
    CantBuildTooCloseToDropOff: _ActionResult.ValueType  # 43
    CantBuildLocationInvalid: _ActionResult.ValueType  # 44
    CantSeeBuildLocation: _ActionResult.ValueType  # 45
    CantBuildTooCloseToCreepSource: _ActionResult.ValueType  # 46
    CantBuildTooCloseToResources: _ActionResult.ValueType  # 47
    CantBuildTooFarFromWater: _ActionResult.ValueType  # 48
    CantBuildTooFarFromCreepSource: _ActionResult.ValueType  # 49
    CantBuildTooFarFromBuildPowerSource: _ActionResult.ValueType  # 50
    CantBuildOnDenseTerrain: _ActionResult.ValueType  # 51
    CantTrainTooFarFromTrainPowerSource: _ActionResult.ValueType  # 52
    CantLandLocationInvalid: _ActionResult.ValueType  # 53
    CantSeeLandLocation: _ActionResult.ValueType  # 54
    CantLandTooCloseToCreepSource: _ActionResult.ValueType  # 55
    CantLandTooCloseToResources: _ActionResult.ValueType  # 56
    CantLandTooFarFromWater: _ActionResult.ValueType  # 57
    CantLandTooFarFromCreepSource: _ActionResult.ValueType  # 58
    CantLandTooFarFromBuildPowerSource: _ActionResult.ValueType  # 59
    CantLandTooFarFromTrainPowerSource: _ActionResult.ValueType  # 60
    CantLandOnDenseTerrain: _ActionResult.ValueType  # 61
    AddOnTooFarFromBuilding: _ActionResult.ValueType  # 62
    MustBuildRefineryFirst: _ActionResult.ValueType  # 63
    BuildingIsUnderConstruction: _ActionResult.ValueType  # 64
    CantFindDropOff: _ActionResult.ValueType  # 65
    CantLoadOtherPlayersUnits: _ActionResult.ValueType  # 66
    NotEnoughRoomToLoadUnit: _ActionResult.ValueType  # 67
    CantUnloadUnitsThere: _ActionResult.ValueType  # 68
    CantWarpInUnitsThere: _ActionResult.ValueType  # 69
    CantLoadImmobileUnits: _ActionResult.ValueType  # 70
    CantRechargeImmobileUnits: _ActionResult.ValueType  # 71
    CantRechargeUnderConstructionUnits: _ActionResult.ValueType  # 72
    CantLoadThatUnit: _ActionResult.ValueType  # 73
    NoCargoToUnload: _ActionResult.ValueType  # 74
    LoadAllNoTargetsFound: _ActionResult.ValueType  # 75
    NotWhileOccupied: _ActionResult.ValueType  # 76
    CantAttackWithoutAmmo: _ActionResult.ValueType  # 77
    CantHoldAnyMoreAmmo: _ActionResult.ValueType  # 78
    TechRequirementsNotMet: _ActionResult.ValueType  # 79
    MustLockdownUnitFirst: _ActionResult.ValueType  # 80
    MustTargetUnit: _ActionResult.ValueType  # 81
    MustTargetInventory: _ActionResult.ValueType  # 82
    MustTargetVisibleUnit: _ActionResult.ValueType  # 83
    MustTargetVisibleLocation: _ActionResult.ValueType  # 84
    MustTargetWalkableLocation: _ActionResult.ValueType  # 85
    MustTargetPawnableUnit: _ActionResult.ValueType  # 86
    YouCantControlThatUnit: _ActionResult.ValueType  # 87
    YouCantIssueCommandsToThatUnit: _ActionResult.ValueType  # 88
    MustTargetResources: _ActionResult.ValueType  # 89
    RequiresHealTarget: _ActionResult.ValueType  # 90
    RequiresRepairTarget: _ActionResult.ValueType  # 91
    NoItemsToDrop: _ActionResult.ValueType  # 92
    CantHoldAnyMoreItems: _ActionResult.ValueType  # 93
    CantHoldThat: _ActionResult.ValueType  # 94
    TargetHasNoInventory: _ActionResult.ValueType  # 95
    CantDropThisItem: _ActionResult.ValueType  # 96
    CantMoveThisItem: _ActionResult.ValueType  # 97
    CantPawnThisUnit: _ActionResult.ValueType  # 98
    MustTargetCaster: _ActionResult.ValueType  # 99
    CantTargetCaster: _ActionResult.ValueType  # 100
    MustTargetOuter: _ActionResult.ValueType  # 101
    CantTargetOuter: _ActionResult.ValueType  # 102
    MustTargetYourOwnUnits: _ActionResult.ValueType  # 103
    CantTargetYourOwnUnits: _ActionResult.ValueType  # 104
    MustTargetFriendlyUnits: _ActionResult.ValueType  # 105
    CantTargetFriendlyUnits: _ActionResult.ValueType  # 106
    MustTargetNeutralUnits: _ActionResult.ValueType  # 107
    CantTargetNeutralUnits: _ActionResult.ValueType  # 108
    MustTargetEnemyUnits: _ActionResult.ValueType  # 109
    CantTargetEnemyUnits: _ActionResult.ValueType  # 110
    MustTargetAirUnits: _ActionResult.ValueType  # 111
    CantTargetAirUnits: _ActionResult.ValueType  # 112
    MustTargetGroundUnits: _ActionResult.ValueType  # 113
    CantTargetGroundUnits: _ActionResult.ValueType  # 114
    MustTargetStructures: _ActionResult.ValueType  # 115
    CantTargetStructures: _ActionResult.ValueType  # 116
    MustTargetLightUnits: _ActionResult.ValueType  # 117
    CantTargetLightUnits: _ActionResult.ValueType  # 118
    MustTargetArmoredUnits: _ActionResult.ValueType  # 119
    CantTargetArmoredUnits: _ActionResult.ValueType  # 120
    MustTargetBiologicalUnits: _ActionResult.ValueType  # 121
    CantTargetBiologicalUnits: _ActionResult.ValueType  # 122
    MustTargetHeroicUnits: _ActionResult.ValueType  # 123
    CantTargetHeroicUnits: _ActionResult.ValueType  # 124
    MustTargetRoboticUnits: _ActionResult.ValueType  # 125
    CantTargetRoboticUnits: _ActionResult.ValueType  # 126
    MustTargetMechanicalUnits: _ActionResult.ValueType  # 127
    CantTargetMechanicalUnits: _ActionResult.ValueType  # 128
    MustTargetPsionicUnits: _ActionResult.ValueType  # 129
    CantTargetPsionicUnits: _ActionResult.ValueType  # 130
    MustTargetMassiveUnits: _ActionResult.ValueType  # 131
    CantTargetMassiveUnits: _ActionResult.ValueType  # 132
    MustTargetMissile: _ActionResult.ValueType  # 133
    CantTargetMissile: _ActionResult.ValueType  # 134
    MustTargetWorkerUnits: _ActionResult.ValueType  # 135
    CantTargetWorkerUnits: _ActionResult.ValueType  # 136
    MustTargetEnergyCapableUnits: _ActionResult.ValueType  # 137
    CantTargetEnergyCapableUnits: _ActionResult.ValueType  # 138
    MustTargetShieldCapableUnits: _ActionResult.ValueType  # 139
    CantTargetShieldCapableUnits: _ActionResult.ValueType  # 140
    MustTargetFlyers: _ActionResult.ValueType  # 141
    CantTargetFlyers: _ActionResult.ValueType  # 142
    MustTargetBuriedUnits: _ActionResult.ValueType  # 143
    CantTargetBuriedUnits: _ActionResult.ValueType  # 144
    MustTargetCloakedUnits: _ActionResult.ValueType  # 145
    CantTargetCloakedUnits: _ActionResult.ValueType  # 146
    MustTargetUnitsInAStasisField: _ActionResult.ValueType  # 147
    CantTargetUnitsInAStasisField: _ActionResult.ValueType  # 148
    MustTargetUnderConstructionUnits: _ActionResult.ValueType  # 149
    CantTargetUnderConstructionUnits: _ActionResult.ValueType  # 150
    MustTargetDeadUnits: _ActionResult.ValueType  # 151
    CantTargetDeadUnits: _ActionResult.ValueType  # 152
    MustTargetRevivableUnits: _ActionResult.ValueType  # 153
    CantTargetRevivableUnits: _ActionResult.ValueType  # 154
    MustTargetHiddenUnits: _ActionResult.ValueType  # 155
    CantTargetHiddenUnits: _ActionResult.ValueType  # 156
    CantRechargeOtherPlayersUnits: _ActionResult.ValueType  # 157
    MustTargetHallucinations: _ActionResult.ValueType  # 158
    CantTargetHallucinations: _ActionResult.ValueType  # 159
    MustTargetInvulnerableUnits: _ActionResult.ValueType  # 160
    CantTargetInvulnerableUnits: _ActionResult.ValueType  # 161
    MustTargetDetectedUnits: _ActionResult.ValueType  # 162
    CantTargetDetectedUnits: _ActionResult.ValueType  # 163
    CantTargetUnitWithEnergy: _ActionResult.ValueType  # 164
    CantTargetUnitWithShields: _ActionResult.ValueType  # 165
    MustTargetUncommandableUnits: _ActionResult.ValueType  # 166
    CantTargetUncommandableUnits: _ActionResult.ValueType  # 167
    MustTargetPreventDefeatUnits: _ActionResult.ValueType  # 168
    CantTargetPreventDefeatUnits: _ActionResult.ValueType  # 169
    MustTargetPreventRevealUnits: _ActionResult.ValueType  # 170
    CantTargetPreventRevealUnits: _ActionResult.ValueType  # 171
    MustTargetPassiveUnits: _ActionResult.ValueType  # 172
    CantTargetPassiveUnits: _ActionResult.ValueType  # 173
    MustTargetStunnedUnits: _ActionResult.ValueType  # 174
    CantTargetStunnedUnits: _ActionResult.ValueType  # 175
    MustTargetSummonedUnits: _ActionResult.ValueType  # 176
    CantTargetSummonedUnits: _ActionResult.ValueType  # 177
    MustTargetUser1: _ActionResult.ValueType  # 178
    CantTargetUser1: _ActionResult.ValueType  # 179
    MustTargetUnstoppableUnits: _ActionResult.ValueType  # 180
    CantTargetUnstoppableUnits: _ActionResult.ValueType  # 181
    MustTargetResistantUnits: _ActionResult.ValueType  # 182
    CantTargetResistantUnits: _ActionResult.ValueType  # 183
    MustTargetDazedUnits: _ActionResult.ValueType  # 184
    CantTargetDazedUnits: _ActionResult.ValueType  # 185
    CantLockdown: _ActionResult.ValueType  # 186
    CantMindControl: _ActionResult.ValueType  # 187
    MustTargetDestructibles: _ActionResult.ValueType  # 188
    CantTargetDestructibles: _ActionResult.ValueType  # 189
    MustTargetItems: _ActionResult.ValueType  # 190
    CantTargetItems: _ActionResult.ValueType  # 191
    NoCalldownAvailable: _ActionResult.ValueType  # 192
    WaypointListFull: _ActionResult.ValueType  # 193
    MustTargetRace: _ActionResult.ValueType  # 194
    CantTargetRace: _ActionResult.ValueType  # 195
    MustTargetSimilarUnits: _ActionResult.ValueType  # 196
    CantTargetSimilarUnits: _ActionResult.ValueType  # 197
    CantFindEnoughTargets: _ActionResult.ValueType  # 198
    AlreadySpawningLarva: _ActionResult.ValueType  # 199
    CantTargetExhaustedResources: _ActionResult.ValueType  # 200
    CantUseMinimap: _ActionResult.ValueType  # 201
    CantUseInfoPanel: _ActionResult.ValueType  # 202
    OrderQueueIsFull: _ActionResult.ValueType  # 203
    CantHarvestThatResource: _ActionResult.ValueType  # 204
    HarvestersNotRequired: _ActionResult.ValueType  # 205
    AlreadyTargeted: _ActionResult.ValueType  # 206
    CantAttackWeaponsDisabled: _ActionResult.ValueType  # 207
    CouldntReachTarget: _ActionResult.ValueType  # 208
    TargetIsOutOfRange: _ActionResult.ValueType  # 209
    TargetIsTooClose: _ActionResult.ValueType  # 210
    TargetIsOutOfArc: _ActionResult.ValueType  # 211
    CantFindTeleportLocation: _ActionResult.ValueType  # 212
    InvalidItemClass: _ActionResult.ValueType  # 213
    CantFindCancelOrder: _ActionResult.ValueType  # 214

class ActionResult(_ActionResult, metaclass=_ActionResultEnumTypeWrapper): ...

Success: ActionResult.ValueType  # 1
NotSupported: ActionResult.ValueType  # 2
Error: ActionResult.ValueType  # 3
CantQueueThatOrder: ActionResult.ValueType  # 4
Retry: ActionResult.ValueType  # 5
Cooldown: ActionResult.ValueType  # 6
QueueIsFull: ActionResult.ValueType  # 7
RallyQueueIsFull: ActionResult.ValueType  # 8
NotEnoughMinerals: ActionResult.ValueType  # 9
NotEnoughVespene: ActionResult.ValueType  # 10
NotEnoughTerrazine: ActionResult.ValueType  # 11
NotEnoughCustom: ActionResult.ValueType  # 12
NotEnoughFood: ActionResult.ValueType  # 13
FoodUsageImpossible: ActionResult.ValueType  # 14
NotEnoughLife: ActionResult.ValueType  # 15
NotEnoughShields: ActionResult.ValueType  # 16
NotEnoughEnergy: ActionResult.ValueType  # 17
LifeSuppressed: ActionResult.ValueType  # 18
ShieldsSuppressed: ActionResult.ValueType  # 19
EnergySuppressed: ActionResult.ValueType  # 20
NotEnoughCharges: ActionResult.ValueType  # 21
CantAddMoreCharges: ActionResult.ValueType  # 22
TooMuchMinerals: ActionResult.ValueType  # 23
TooMuchVespene: ActionResult.ValueType  # 24
TooMuchTerrazine: ActionResult.ValueType  # 25
TooMuchCustom: ActionResult.ValueType  # 26
TooMuchFood: ActionResult.ValueType  # 27
TooMuchLife: ActionResult.ValueType  # 28
TooMuchShields: ActionResult.ValueType  # 29
TooMuchEnergy: ActionResult.ValueType  # 30
MustTargetUnitWithLife: ActionResult.ValueType  # 31
MustTargetUnitWithShields: ActionResult.ValueType  # 32
MustTargetUnitWithEnergy: ActionResult.ValueType  # 33
CantTrade: ActionResult.ValueType  # 34
CantSpend: ActionResult.ValueType  # 35
CantTargetThatUnit: ActionResult.ValueType  # 36
CouldntAllocateUnit: ActionResult.ValueType  # 37
UnitCantMove: ActionResult.ValueType  # 38
TransportIsHoldingPosition: ActionResult.ValueType  # 39
BuildTechRequirementsNotMet: ActionResult.ValueType  # 40
CantFindPlacementLocation: ActionResult.ValueType  # 41
CantBuildOnThat: ActionResult.ValueType  # 42
CantBuildTooCloseToDropOff: ActionResult.ValueType  # 43
CantBuildLocationInvalid: ActionResult.ValueType  # 44
CantSeeBuildLocation: ActionResult.ValueType  # 45
CantBuildTooCloseToCreepSource: ActionResult.ValueType  # 46
CantBuildTooCloseToResources: ActionResult.ValueType  # 47
CantBuildTooFarFromWater: ActionResult.ValueType  # 48
CantBuildTooFarFromCreepSource: ActionResult.ValueType  # 49
CantBuildTooFarFromBuildPowerSource: ActionResult.ValueType  # 50
CantBuildOnDenseTerrain: ActionResult.ValueType  # 51
CantTrainTooFarFromTrainPowerSource: ActionResult.ValueType  # 52
CantLandLocationInvalid: ActionResult.ValueType  # 53
CantSeeLandLocation: ActionResult.ValueType  # 54
CantLandTooCloseToCreepSource: ActionResult.ValueType  # 55
CantLandTooCloseToResources: ActionResult.ValueType  # 56
CantLandTooFarFromWater: ActionResult.ValueType  # 57
CantLandTooFarFromCreepSource: ActionResult.ValueType  # 58
CantLandTooFarFromBuildPowerSource: ActionResult.ValueType  # 59
CantLandTooFarFromTrainPowerSource: ActionResult.ValueType  # 60
CantLandOnDenseTerrain: ActionResult.ValueType  # 61
AddOnTooFarFromBuilding: ActionResult.ValueType  # 62
MustBuildRefineryFirst: ActionResult.ValueType  # 63
BuildingIsUnderConstruction: ActionResult.ValueType  # 64
CantFindDropOff: ActionResult.ValueType  # 65
CantLoadOtherPlayersUnits: ActionResult.ValueType  # 66
NotEnoughRoomToLoadUnit: ActionResult.ValueType  # 67
CantUnloadUnitsThere: ActionResult.ValueType  # 68
CantWarpInUnitsThere: ActionResult.ValueType  # 69
CantLoadImmobileUnits: ActionResult.ValueType  # 70
CantRechargeImmobileUnits: ActionResult.ValueType  # 71
CantRechargeUnderConstructionUnits: ActionResult.ValueType  # 72
CantLoadThatUnit: ActionResult.ValueType  # 73
NoCargoToUnload: ActionResult.ValueType  # 74
LoadAllNoTargetsFound: ActionResult.ValueType  # 75
NotWhileOccupied: ActionResult.ValueType  # 76
CantAttackWithoutAmmo: ActionResult.ValueType  # 77
CantHoldAnyMoreAmmo: ActionResult.ValueType  # 78
TechRequirementsNotMet: ActionResult.ValueType  # 79
MustLockdownUnitFirst: ActionResult.ValueType  # 80
MustTargetUnit: ActionResult.ValueType  # 81
MustTargetInventory: ActionResult.ValueType  # 82
MustTargetVisibleUnit: ActionResult.ValueType  # 83
MustTargetVisibleLocation: ActionResult.ValueType  # 84
MustTargetWalkableLocation: ActionResult.ValueType  # 85
MustTargetPawnableUnit: ActionResult.ValueType  # 86
YouCantControlThatUnit: ActionResult.ValueType  # 87
YouCantIssueCommandsToThatUnit: ActionResult.ValueType  # 88
MustTargetResources: ActionResult.ValueType  # 89
RequiresHealTarget: ActionResult.ValueType  # 90
RequiresRepairTarget: ActionResult.ValueType  # 91
NoItemsToDrop: ActionResult.ValueType  # 92
CantHoldAnyMoreItems: ActionResult.ValueType  # 93
CantHoldThat: ActionResult.ValueType  # 94
TargetHasNoInventory: ActionResult.ValueType  # 95
CantDropThisItem: ActionResult.ValueType  # 96
CantMoveThisItem: ActionResult.ValueType  # 97
CantPawnThisUnit: ActionResult.ValueType  # 98
MustTargetCaster: ActionResult.ValueType  # 99
CantTargetCaster: ActionResult.ValueType  # 100
MustTargetOuter: ActionResult.ValueType  # 101
CantTargetOuter: ActionResult.ValueType  # 102
MustTargetYourOwnUnits: ActionResult.ValueType  # 103
CantTargetYourOwnUnits: ActionResult.ValueType  # 104
MustTargetFriendlyUnits: ActionResult.ValueType  # 105
CantTargetFriendlyUnits: ActionResult.ValueType  # 106
MustTargetNeutralUnits: ActionResult.ValueType  # 107
CantTargetNeutralUnits: ActionResult.ValueType  # 108
MustTargetEnemyUnits: ActionResult.ValueType  # 109
CantTargetEnemyUnits: ActionResult.ValueType  # 110
MustTargetAirUnits: ActionResult.ValueType  # 111
CantTargetAirUnits: ActionResult.ValueType  # 112
MustTargetGroundUnits: ActionResult.ValueType  # 113
CantTargetGroundUnits: ActionResult.ValueType  # 114
MustTargetStructures: ActionResult.ValueType  # 115
CantTargetStructures: ActionResult.ValueType  # 116
MustTargetLightUnits: ActionResult.ValueType  # 117
CantTargetLightUnits: ActionResult.ValueType  # 118
MustTargetArmoredUnits: ActionResult.ValueType  # 119
CantTargetArmoredUnits: ActionResult.ValueType  # 120
MustTargetBiologicalUnits: ActionResult.ValueType  # 121
CantTargetBiologicalUnits: ActionResult.ValueType  # 122
MustTargetHeroicUnits: ActionResult.ValueType  # 123
CantTargetHeroicUnits: ActionResult.ValueType  # 124
MustTargetRoboticUnits: ActionResult.ValueType  # 125
CantTargetRoboticUnits: ActionResult.ValueType  # 126
MustTargetMechanicalUnits: ActionResult.ValueType  # 127
CantTargetMechanicalUnits: ActionResult.ValueType  # 128
MustTargetPsionicUnits: ActionResult.ValueType  # 129
CantTargetPsionicUnits: ActionResult.ValueType  # 130
MustTargetMassiveUnits: ActionResult.ValueType  # 131
CantTargetMassiveUnits: ActionResult.ValueType  # 132
MustTargetMissile: ActionResult.ValueType  # 133
CantTargetMissile: ActionResult.ValueType  # 134
MustTargetWorkerUnits: ActionResult.ValueType  # 135
CantTargetWorkerUnits: ActionResult.ValueType  # 136
MustTargetEnergyCapableUnits: ActionResult.ValueType  # 137
CantTargetEnergyCapableUnits: ActionResult.ValueType  # 138
MustTargetShieldCapableUnits: ActionResult.ValueType  # 139
CantTargetShieldCapableUnits: ActionResult.ValueType  # 140
MustTargetFlyers: ActionResult.ValueType  # 141
CantTargetFlyers: ActionResult.ValueType  # 142
MustTargetBuriedUnits: ActionResult.ValueType  # 143
CantTargetBuriedUnits: ActionResult.ValueType  # 144
MustTargetCloakedUnits: ActionResult.ValueType  # 145
CantTargetCloakedUnits: ActionResult.ValueType  # 146
MustTargetUnitsInAStasisField: ActionResult.ValueType  # 147
CantTargetUnitsInAStasisField: ActionResult.ValueType  # 148
MustTargetUnderConstructionUnits: ActionResult.ValueType  # 149
CantTargetUnderConstructionUnits: ActionResult.ValueType  # 150
MustTargetDeadUnits: ActionResult.ValueType  # 151
CantTargetDeadUnits: ActionResult.ValueType  # 152
MustTargetRevivableUnits: ActionResult.ValueType  # 153
CantTargetRevivableUnits: ActionResult.ValueType  # 154
MustTargetHiddenUnits: ActionResult.ValueType  # 155
CantTargetHiddenUnits: ActionResult.ValueType  # 156
CantRechargeOtherPlayersUnits: ActionResult.ValueType  # 157
MustTargetHallucinations: ActionResult.ValueType  # 158
CantTargetHallucinations: ActionResult.ValueType  # 159
MustTargetInvulnerableUnits: ActionResult.ValueType  # 160
CantTargetInvulnerableUnits: ActionResult.ValueType  # 161
MustTargetDetectedUnits: ActionResult.ValueType  # 162
CantTargetDetectedUnits: ActionResult.ValueType  # 163
CantTargetUnitWithEnergy: ActionResult.ValueType  # 164
CantTargetUnitWithShields: ActionResult.ValueType  # 165
MustTargetUncommandableUnits: ActionResult.ValueType  # 166
CantTargetUncommandableUnits: ActionResult.ValueType  # 167
MustTargetPreventDefeatUnits: ActionResult.ValueType  # 168
CantTargetPreventDefeatUnits: ActionResult.ValueType  # 169
MustTargetPreventRevealUnits: ActionResult.ValueType  # 170
CantTargetPreventRevealUnits: ActionResult.ValueType  # 171
MustTargetPassiveUnits: ActionResult.ValueType  # 172
CantTargetPassiveUnits: ActionResult.ValueType  # 173
MustTargetStunnedUnits: ActionResult.ValueType  # 174
CantTargetStunnedUnits: ActionResult.ValueType  # 175
MustTargetSummonedUnits: ActionResult.ValueType  # 176
CantTargetSummonedUnits: ActionResult.ValueType  # 177
MustTargetUser1: ActionResult.ValueType  # 178
CantTargetUser1: ActionResult.ValueType  # 179
MustTargetUnstoppableUnits: ActionResult.ValueType  # 180
CantTargetUnstoppableUnits: ActionResult.ValueType  # 181
MustTargetResistantUnits: ActionResult.ValueType  # 182
CantTargetResistantUnits: ActionResult.ValueType  # 183
MustTargetDazedUnits: ActionResult.ValueType  # 184
CantTargetDazedUnits: ActionResult.ValueType  # 185
CantLockdown: ActionResult.ValueType  # 186
CantMindControl: ActionResult.ValueType  # 187
MustTargetDestructibles: ActionResult.ValueType  # 188
CantTargetDestructibles: ActionResult.ValueType  # 189
MustTargetItems: ActionResult.ValueType  # 190
CantTargetItems: ActionResult.ValueType  # 191
NoCalldownAvailable: ActionResult.ValueType  # 192
WaypointListFull: ActionResult.ValueType  # 193
MustTargetRace: ActionResult.ValueType  # 194
CantTargetRace: ActionResult.ValueType  # 195
MustTargetSimilarUnits: ActionResult.ValueType  # 196
CantTargetSimilarUnits: ActionResult.ValueType  # 197
CantFindEnoughTargets: ActionResult.ValueType  # 198
AlreadySpawningLarva: ActionResult.ValueType  # 199
CantTargetExhaustedResources: ActionResult.ValueType  # 200
CantUseMinimap: ActionResult.ValueType  # 201
CantUseInfoPanel: ActionResult.ValueType  # 202
OrderQueueIsFull: ActionResult.ValueType  # 203
CantHarvestThatResource: ActionResult.ValueType  # 204
HarvestersNotRequired: ActionResult.ValueType  # 205
AlreadyTargeted: ActionResult.ValueType  # 206
CantAttackWeaponsDisabled: ActionResult.ValueType  # 207
CouldntReachTarget: ActionResult.ValueType  # 208
TargetIsOutOfRange: ActionResult.ValueType  # 209
TargetIsTooClose: ActionResult.ValueType  # 210
TargetIsOutOfArc: ActionResult.ValueType  # 211
CantFindTeleportLocation: ActionResult.ValueType  # 212
InvalidItemClass: ActionResult.ValueType  # 213
CantFindCancelOrder: ActionResult.ValueType  # 214
global___ActionResult = ActionResult
