#!/system/bin/sh
# ==================================================
# init.oplus.cota.sh - Stub for Oplus/Realme COTA handling
# Used in LineageOS builds to replace proprietary commands
# ==================================================

LOGTAG="oplus_cota_stub"

log -t $LOGTAG "Creating /data/cota directory if missing..."
mkdir -p /data/cota
chown root:cache /data/cota
chmod 0770 /data/cota
restorecon /data/cota

log -t $LOGTAG "COTA stub executed successfully."
exit 0
