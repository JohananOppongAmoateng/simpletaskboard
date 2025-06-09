#!/bin/bash

echo "🔍 Checking DJANGO_SETTINGS_MODULE..."

if [[ "$DJANGO_SETTINGS_MODULE" != "config.settings.test" && "$DJANGO_SETTINGS_MODULE" != "" ]]; then
  echo "⚠️  DJANGO_SETTINGS_MODULE is set to '$DJANGO_SETTINGS_MODULE'"
  echo "🧹 Unsetting DJANGO_SETTINGS_MODULE for this session..."
  unset DJANGO_SETTINGS_MODULE
else
  echo "✅ DJANGO_SETTINGS_MODULE is clean or correctly set."
fi

echo -e "\n🚀 Now run your tests:\n   pytest\n"
