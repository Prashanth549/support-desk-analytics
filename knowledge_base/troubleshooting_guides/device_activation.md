# Device Activation Troubleshooting Guide

**Category:** Technical Support  
**Difficulty:** Beginner to Intermediate  
**Average Resolution Time:** 15-25 minutes  
**Last Updated:** February 2024

---

## Overview

Device activation is the process of registering a new device on the network. This guide covers activation for new phones, SIM swaps, and device upgrades.

---

## Prerequisites

Before starting activation:

✅ **Account Requirements:**
- Account in good standing
- No past-due balance
- Device compatible with network
- SIM card provisioned to account

✅ **Customer Should Have:**
- New device powered on
- SIM card (either pre-installed or separate)
- Wi-Fi connection (helpful but not required)
- Device unlocked (if bringing own device)

---

## Activation Methods

### Method 1: Automatic Activation (Preferred)

**When to use:** Brand new devices from carrier

**Steps:**
1. Insert SIM card into device
2. Power on device
3. Connect to Wi-Fi
4. Device will automatically activate (usually 2-5 minutes)
5. Look for signal bars in status bar

**Success indicators:**
- Signal bars appear (5G, LTE, or bars icon)
- Can make test call
- Can send/receive text

**If fails:** Proceed to Method 2

---

### Method 2: Manual Activation via Settings

**When to use:** Automatic activation didn't complete

#### For iPhone:
```
1. Settings → General → About
2. Wait 30 seconds - may see "Carrier Settings Update" popup
3. If popup appears, tap "Update"
4. Wait 2 minutes
5. Test signal

If no popup after 1 minute:
Settings → General → Transfer or Reset iPhone → 
Reset → Reset Network Settings
```

#### For Android:
```
1. Settings → About Phone → Status → IMEI
   - Note down IMEI number
2. Settings → Network & Internet → Mobile Network
3. Look for "Carrier Services" or "Activate Device"
4. If available, tap and follow prompts
5. Test signal

Alternative method:
Dial: *#*#4636#*#*
Tap: "Phone Information"
Scroll down: Look for "Set Preferred Network Type"
Select: "LTE/WCDMA"
Restart device
```

---

### Method 3: Manual Activation via System

**When to use:** Methods 1 & 2 failed, or BYOD (Bring Your Own Device)

**Required information:**
- IMEI (dial *#06# to display)
- SIM card number (ICCID - on SIM card)
- Account PIN or last 4 of SSN

**System steps:**
```
1. Log into activation portal
2. Enter customer account number
3. Select "Add Device" or "Activate Device"
4. Enter IMEI: [customer provides]
5. Enter SIM ICCID: [on SIM card or packaging]
6. Confirm device make/model matches
7. Submit activation request
8. Wait for confirmation (usually instant)
9. Have customer restart device
10. Verify signal bars appear
```

**If system error:** Note error code, escalate to provisioning team

---

## Common Issues & Solutions

### Issue 1: "SIM Not Provisioned" or Error Code 404

**Root Cause:** SIM card not activated in system

**Solution:**
1. Verify SIM ICCID matches account
2. Check SIM status in system (should show "Active")
3. If showing "Inventory" or "Inactive":
   - Provision SIM to account
   - Wait 2 minutes
   - Restart device

**If persists:** SIM may be defective, requires replacement

---

### Issue 2: "No Service" After Activation

**Root Cause:** Device not registering on network

**Solution:**
```
1. Verify device is carrier-unlocked (if BYOD)
2. Check IMEI is not blacklisted:
   - Run IMEI check in system
   - If blacklisted: Cannot activate (fraud/lost/stolen)
3. Verify device compatible:
   - Must support network bands
   - Check compatibility tool
4. Reset network settings (see Method 2)
```

---

### Issue 3: "Activation Pending" for Over 30 Minutes

**Root Cause:** Backend provisioning delay

**Solution:**
1. Check activation queue in system
2. If stuck in queue:
   - Cancel pending activation
   - Wait 5 minutes
   - Resubmit activation
3. If still stuck:
   - Clear device from system
   - Re-add device as new activation
   - Escalate to provisioning if continues

---

### Issue 4: SIM Card Not Detected

**Root Cause:** Physical SIM issue or tray problem

**Solution:**
```
1. Power off device completely
2. Remove SIM card
3. Inspect SIM:
   - Check for damage, scratches
   - Verify correct size (nano, micro, standard)
4. Inspect SIM tray:
   - Check for debris
   - Ensure tray not bent
5. Clean SIM contacts with dry cloth
6. Reinsert firmly (should click in place)
7. Power on device
8. Wait 1 minute for detection
```

**If still not detected:**
- Try SIM in different device (if available)
- If works in other device: Customer's SIM slot issue (hardware repair)
- If doesn't work: SIM defective (send replacement)

---

### Issue 5: Error "IMEI Already in Use"

**Root Cause:** Device still associated with previous account

**Solution:**
1. Verify customer owns device (not stolen/fraud)
2. Check previous account:
   - If customer's old account: Remove device from old line
   - If different customer: Cannot activate (security issue)
3. If device legitimately purchased used:
   - Request proof of purchase
   - Escalate to fraud team for clearance
   - May take 24-48 hours

---

## Special Scenarios

### Scenario: iPhone eSIM Activation

**Process:**
```
1. Customer receives eSIM QR code via email
2. Settings → Mobile Data → Add Data Plan
3. Scan QR code or enter details manually
4. Follow on-screen prompts
5. Primary line/secondary line selection
6. Wait for activation (2-5 minutes)
7. Test both voice and data
```

**Troubleshooting eSIM:**
- Delete failed eSIM profile before retry
- Ensure iOS 12.1 or later
- Device must be carrier-unlocked

---

### Scenario: Tablet/Wearable Activation

**Differences from phone:**
- Data-only plan (usually)
- May not support voice calls
- Wearables often paired to phone number

**Steps:**
1. Verify device type in system
2. Ensure data-only plan assigned
3. Follow manufacturer's activation app
4. Test data connection only

---

## Quality Checklist

Before closing activation ticket:

- [ ] Customer confirms signal bars visible
- [ ] Test outbound call successful
- [ ] Test inbound call successful (call customer back)
- [ ] Test SMS send/receive
- [ ] Test mobile data (have customer open website)
- [ ] Verify voicemail set up (if new line)
- [ ] Educate on Wi-Fi calling (if available)
- [ ] Document IMEI in ticket notes

---

## Escalation Path

**Escalate to Provisioning Team if:**
- Activation fails after 3 attempts
- System errors preventing activation
- IMEI or SIM issues in backend
- Device compatibility questions

**Escalate to Technical Support if:**
- Device hardware suspected (SIM slot, antenna)
- Software issues (OS bugs, carrier bundle)

**Required escalation info:**
- Account number
- Device IMEI
- SIM ICCID
- All troubleshooting steps attempted
- Screenshots of errors (if available)

---

## Tips for Success

1. **Always verify basics first:** SIM seated, device powered on, account active
2. **Be patient:** Some activations take up to 10 minutes
3. **Restart is your friend:** Solves 50%+ of activation issues
4. **Document everything:** IMEI, SIM, error codes, steps tried
5. **Set expectations:** Explain that activation usually takes 5-10 minutes

---

## Related Guides

- [Network Connectivity Troubleshooting](network_connectivity.md)
- [SIM Card Issues](../common_issues.md#sim-card-issues)

---

**Author:** Support Training Team  
**Last Review:** February 13, 2024  
**Next Review:** May 13, 2024
```

Save this file.

---

## ✅ Checkpoint 5

**Knowledge Base Created:**
```
knowledge_base/
├── common_issues.md                              ← Quick reference
└── troubleshooting_guides/
    ├── network_connectivity.md                   ← Detailed guide 1
    └── device_activation.md                      ← Detailed guide 2