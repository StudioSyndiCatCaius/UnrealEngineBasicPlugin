// Fill out your copyright notice in the Description page of Project Settings.


#include "StarterFactory.h"

UStarterFactory::UStarterFactory()
{
	SupportedClass = UStarter::StaticClass();
	bCreateNew = true;
}

UObject* UStarterFactory::FactoryCreateNew(UClass* Class, UObject* InParent, FName Name, EObjectFlags Flags,
                                               UObject* Context, FFeedbackContext* Warn)
{
	return NewObject<UStarter>(InParent, Class, Name, Flags, Context);
}
