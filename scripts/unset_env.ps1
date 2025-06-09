Write-Output "🔍 Checking DJANGO_SETTINGS_MODULE..."

if ($env:DJANGO_SETTINGS_MODULE -and $env:DJANGO_SETTINGS_MODULE -ne "config.settings.test") {
    Write-Output "⚠️  DJANGO_SETTINGS_MODULE is set to '$env:DJANGO_SETTINGS_MODULE'"
    Write-Output "🧹 Unsetting it..."
    Remove-Item Env:DJANGO_SETTINGS_MODULE
} else {
    Write-Output "✅ DJANGO_SETTINGS_MODULE is clean or correctly set."
}

Write-Output "`n🚀 Now run your tests:`n   pytest"
