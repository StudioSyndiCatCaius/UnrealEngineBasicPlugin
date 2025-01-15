// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "AssetTypeActions_Base.h"
#include "Starter.h"
#include "Factories/Factory.h"
#include "StarterFactory.generated.h"


class FStarterAssetTypeActions : public FAssetTypeActions_Base
{
public:
	UClass* GetSupportedClass() const override {return UStarter::StaticClass();};
	FText GetName() const override { return INVTEXT("Actor Preset"); };
	FColor GetTypeColor() const override {return FColor::Cyan;};
	uint32 GetCategories() override { return EAssetTypeCategories::Misc; };
};


UCLASS()
class STARTEREDITORMODULE_API UStarterFactory : public UFactory
{
	GENERATED_BODY()
public:
	UStarterFactory();
	UObject* FactoryCreateNew(UClass* Class, UObject* InParent, FName Name, EObjectFlags Flags, UObject* Context, FFeedbackContext* Warn);
};

