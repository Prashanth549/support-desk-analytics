# Network Connectivity Troubleshooting Guide

**Category:** Technical Support  
**Difficulty:** Intermediate  
**Average Resolution Time:** 20-30 minutes  
**Last Updated:** February 2024

---

## Table of Contents
1. [Overview](#overview)
2. [Common Symptoms](#common-symptoms)
3. [Diagnostic Steps](#diagnostic-steps)
4. [Resolution Procedures](#resolution-procedures)
5. [Escalation Criteria](#escalation-criteria)
6. [Prevention Tips](#prevention-tips)

---

## Overview

Network connectivity issues are among the most common support requests. This guide covers troubleshooting for 5G, LTE, and general mobile data connectivity problems.

**What You'll Need:**
- Customer's device model and OS version
- Current location (city/area)
- Network type showing on device (5G, LTE, 3G, etc.)
- Duration of issue

---

## Common Symptoms

### Symptom 1: "No Service" or "Searching"
**What it means:** Device cannot connect to any network
**Common causes:**
- SIM card not properly seated
- Network outage in area
- Device in airplane mode
- Account suspended/inactive

### Symptom 2: "5G Not Connecting"
**What it means:** Device shows LTE but not 5G
**Common causes:**
- Not in 5G coverage area
- 5G disabled in settings
- Device not 5G compatible
- Network congestion

### Symptom 3: "Connected But No Internet"
**What it means:** Shows network bars but data doesn't work
**Common causes:**
- Data plan exhausted/throttled
- APN settings incorrect
- iOS data toggle disabled
- Network authentication issue

---

## Diagnostic Steps

### Step 1: Verify Basic Information
```
Questions to Ask:
1. When did the issue start?
2. Does it happen everywhere or specific locations?
3. Have you traveled recently?
4. Any recent device updates or changes?
5. Does Wi-Fi work normally?
```

**Document in ticket:** Location, timing, consistency of issue

---

### Step 2: Check Account Status
```sql
-- Verify in system:
- Account active and in good standing
- Data plan active
- No temporary suspensions
- Device IMEI matches account
```

**If account issues found:** Resolve account status before troubleshooting device

---

### Step 3: Check Network Coverage

1. Verify customer location is in coverage area
2. Check tower status in area (use internal tools)
3. Look for any known outages

**If tower issue:** Document ticket, set expectation for resolution timeline

---

### Step 4: Device-Level Diagnostics

#### For iPhone:
```
1. Settings → Mobile Data → verify ON
2. Settings → Mobile Data → Mobile Data Options → Voice & Data
   - Check if 5G is selected
3. Settings → Mobile Data → Mobile Data Network
   - Verify APN settings
```

#### For Android:
```
1. Settings → Network & Internet → Mobile Network → verify ON
2. Settings → Network & Internet → Mobile Network → Preferred network type
   - Should show "5G/LTE/3G/2G (auto)"
3. Settings → Network & Internet → Mobile Network → Access Point Names
   - Verify correct APN
```

---

## Resolution Procedures

### Procedure 1: Basic Reset (Success Rate: 60%)

**Steps:**
1. Toggle Airplane Mode ON for 10 seconds
2. Toggle Airplane Mode OFF
3. Wait 30 seconds for network registration
4. Test data connection (open browser, load webpage)

**If successful:** Document resolution, close ticket
**If unsuccessful:** Proceed to Procedure 2

---

### Procedure 2: Network Settings Reset (Success Rate: 80%)

#### iPhone:
```
Settings → General → Transfer or Reset iPhone → 
Reset → Reset Network Settings

⚠️ Warning: This clears Wi-Fi passwords
```

#### Android:
```
Settings → System → Reset Options → 
Reset Wi-Fi, mobile & Bluetooth

⚠️ Warning: This clears saved networks
```

**After reset:**
1. Device will restart automatically
2. Wait 1-2 minutes for network registration
3. Verify data connection works
4. Reconnect to Wi-Fi networks if needed

**If successful:** Document resolution, educate customer
**If unsuccessful:** Proceed to Procedure 3

---

### Procedure 3: Manual Network Selection (Success Rate: 70%)

**Use when:** Traveling, border areas, or network handoff issues

#### Steps:
1. **Turn OFF automatic network selection**
   - iPhone: Settings → Mobile Data → Network Selection → OFF
   - Android: Settings → Network & Internet → Mobile Network → Automatically select network → OFF

2. **Wait for network scan** (may take 30-60 seconds)

3. **Select correct carrier manually**
   - Look for carrier name + "5G" or "LTE"

4. **Test connection**

5. **Turn automatic back ON** (after confirming it works)

**If successful:** Document, advise customer to use auto in the future
**If unsuccessful:** Proceed to escalation

---

### Procedure 4: APN Configuration (Advanced)

**Use when:** All above failed, data specifically not working

#### Correct APN Settings:
```
Name: [Carrier Name] Internet
APN: internet
Proxy: Not set
Port: Not set
Username: Not set
Password: Not set
MMS Proxy: Not set
MMS Port: Not set
Authentication Type: None
APN Type: default,supl,mms
APN Protocol: IPv4/IPv6
```

**To send APN via SMS:**
1. Use internal provisioning tool
2. Send configuration SMS to customer
3. Customer taps notification to install
4. Restart device
5. Test data connection

---

## Escalation Criteria

### Escalate to Engineering if:

- ✅ No service despite SIM working in different device
- ✅ Multiple customers reporting issue in same area
- ✅ Tower shows offline in system
- ✅ All troubleshooting procedures failed
- ✅ Account provisioning errors in backend

### Escalate to Supervisor if:

- ✅ Customer requests compensation for extended outage
- ✅ Business account with SLA requirements
- ✅ Issue ongoing for more than 48 hours

### Documentation for Escalation:
```
Required Information:
1. Customer account number
2. Device make/model/IMEI
3. Exact location where issue occurs
4. All troubleshooting steps attempted
5. Error messages or screenshots if available
6. Duration of issue
```

---

## Prevention Tips

### Educate Customers:

1. **Keep iOS/Android updated** - Carrier settings updates included
2. **Restart device weekly** - Clears temporary network glitches
3. **Wi-Fi Calling setup** - Backup for poor coverage areas
4. **Coverage map awareness** - Understand 5G vs LTE availability

### Proactive Monitoring:

- Check for iOS/Android updates causing known issues
- Monitor tower maintenance schedules
- Track repeat callers from specific zip codes

---

## Related Articles

- [Device Activation Guide](device_activation.md)
- [5G Home Internet Setup](5g_home_internet.md)
- [Common Issues Quick Reference](../common_issues.md)

---

## Revision History

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2024-02-13 | 1.0 | Initial creation | Support Team |

---

**Questions or improvements?** Contact: priya.sharma@support.com