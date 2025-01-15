// Copyright Epic Games, Inc. All Rights Reserved.

#include "StarterEditorModule.h"

#include "StarterFactory.h"

#define LOCTEXT_NAMESPACE "FStarterEditorModule"

void FStarterEditorModule::StartupModule()
{
	TSharedPtr<FStarterAssetTypeActions> AssetTypeActions_ActorPrefab = MakeShared<FStarterAssetTypeActions>();
	FAssetToolsModule::GetModule().Get().RegisterAssetTypeActions(AssetTypeActions_ActorPrefab.ToSharedRef());
	// This code will execute after your module is loaded into memory; the exact timing is specified in the .uplugin file per-module
}

void FStarterEditorModule::ShutdownModule()
{
	// This function may be called during shutdown to clean up your module.  For modules that support dynamic reloading,
	// we call this function before unloading the module.
}

#undef LOCTEXT_NAMESPACE
	
IMPLEMENT_MODULE(FStarterEditorModule, StarterEditor)