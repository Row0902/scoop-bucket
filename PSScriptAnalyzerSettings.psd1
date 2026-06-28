@{
    Severity     = @('Error', 'Warning')
    IncludeRules = @(
        'DSCDscExamplesPresent'
        'DSCDscTestsPresent'
        'DSCReturnCorrectTypesForDSCFunctions'
        'DSCStandardDSCFunctionsInResource'
        'DSCUseIdenticalMandatoryParametersForDSC'
        'DSCUseIdenticalParametersForDSC'
        'PSAvoidDefaultValueSwitchParameter'
        'PSAvoidGlobalVars'
        'PSAvoidTrailingWhitespace'
        'PSAvoidUsingCmdletAliases'
        'PSAvoidUsingPositionalParameters'
        'PSMisleadingBacktick'
        'PSMissingModuleManifestField'
        'PSReservedCmdletChar'
        'PSReservedParams'
        'PSShouldProcess'
        'PSUseApprovedVerbs'
        'PSUseDeclaredVarsMoreThanAssignments'
        'PSUseOutputTypeCorrectly'
        'PSUsePSCredentialType'
        'PSUseShouldProcessForStateChangingFunctions'
    )
}
