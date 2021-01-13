================================================================================
Release Notes
================================================================================

QuickMigrate (A tool to enable migration from OpenManage Essentials to OpenManage Enterprise)

The QuickMigrate tool enables the migration of various settings configured in the OpenManage Essentials to the OpenManage Enterprise appliance.


--------------------------------------------------------------------------------
Version: QuickMigrate 1.0

--------------------------------------------------------------------------------
Release Date: September 2019

--------------------------------------------------------------------------------
Previous Version: NA

--------------------------------------------------------------------------------

================================================================================
What’s New?
================================================================================
 
* Support for the following features in the first release:
  - Installation of the tool in an existing Windows system. It is recommended to install the tool on the same system as OpenManage Essentials.
  - Support for connecting to OpenManage Essentials using Windows or SQL authentication.
  - The following settings can be migrated from OpenManage Essentials to OpenManage Enterprise using this version of the tool:
	-SMTP settings (SMTP server, Credentials).
	-Proxy setings (Proxy server, credentials).
	-Discovery ranges with different formats.
	-Online catalog.
	-Query groups.
  
================================================================================
Known Issues
================================================================================

1. OpenManage Essentials supports different credentials for chassis and sleds for PowerEdge M1000e, PowerEdge FX2s, PowerEdge VRTX and PowerEdge MX7000. However, in OpenManage Enterprise the complete chassis discovery can be done only through chassis credentials. During migration, only chassis credentials will be migrated and used for discovery in OpenManage Enterprise.

2. OpenManage Essentials does not have an option to provide IOA credentials during discovery. As a result, when any discovery range for chassis is migrated, the IOA discovery will be done in OpenManage Enterprise using chassis credentials. If the IOAs have different credentials, user has to edit the discovery range in OpenManage Enterprise and provide the credentials. This is required for VLAN deployment.

3. Discovery ranges with protocols unsupported in OpenManage Enterprise will be dropped during migration.(For example, WMI).

4. If a WSMAN discovery range is created in OpenManage Essentials with certificates, the migrated range in OpenManage Enterprise will fail to discover the device. User has to manually edit the job and provide the certificates in OpenManage Enterprise.

5. While the migration is in progress, do not click the "Back" and the "Next" button. This might result in migration failure.

6. A discovery range created in OpenManage Essentials for VMWare ESX will be shown as a WSMAN credentials range in tool's GUI. This is because OpenManage Essentials supports the discovery using WSMAN. While migration, this will be automatically converted to appropriate protocol.

7. If you see a connection failure to database from the tool's GUI, please attempt again. If the connection is still unsuccesful verify the connection 
using any SQL tools (SQL Management studio, UDL etc.)

8. If Ctrl+Tab key sequence is used in tool's GUI, it might produce undesirable results during navigation. It is recommended to use mouse clicks.

9. After uninstalling the tool, "Logs" folder will not be removed. It can be deleted manually.

10. If you see any connection errors to OpenManage Essentials Database or OpenManage Enterprise appliance, check the connectivity and restart the tool.

11. If you have used the the "domain\username" format to discover Dell iDRACs in OpenManage Essentials, the ranges will be migrated but the discovery may fail in OpenManage Enterprise. Edit the ranges in OpenManage Enterprise to use "username@domain" format.

12. If a catalog is already downloaded in OpenManage Enterprise, the migration will fail. However, this can be safely ignored.

13. The column numbering in the discovery range configuration page may show irregularity.

14. If the number of discovery ranges are more than 50, the "Provide individual credentials for discovery ranges" page will be comparatively slower.

15. During the migration of query groups, if the attribute "Device Name" is used for any query in OpenManage Essentials it may not be migrated correctly.
	To fix the issue, edit the migrated query group in OpenManage Enterprise and select the "Device Name" attribute under Device general info table.
	
16. If one or more discovery ranges and query groups fail to migrate from OpenManage Essentials, the overall status of migration is shown as failed. However,
	the tool will migrate the remaining discovery ranges and query groups.
	
17. If a query group in OpenManage Essentials contains some attributes that are unsupported in OpenManage Enterprise, those query groups will not be migrated.

18. During the migration from OpenManage Essentials if a query group with same name is found on OpenManage Enterprise, migration of some of the query groups will fail.

19. If OpenManage Essentials contains few discovery ranges where multiple unsupported protocols (in OpenManage Enterprise) are selected, the migration of some of the
	discovery ranges will fail. Delete those ranges from OpenManage Essentials and retry the migration.


================================================================================
Installation
================================================================================
--------------------------------------------------------------------------------
Prerequisites
--------------------------------------------------------------------------------

The tool can be installed on all the operating systems supported by OpenManage Essentials.
Latest .NET framework needs to be installed for the tool to function. It is recommended to install the tool on the same system as OpenManage Essentials.

Minimum versions supported:

1. OpenManage Essentials version 2.5.0.
2. OpenManage Enterprise version 3.2.1.

--------------------------------------------------------------------------------
Installation Instructions
--------------------------------------------------------------------------------
The installation is fairly simple. Just double click on the executable and follow the screens. The tool will install in the "Desktop" folder.

  
================================================================================
Instructions to Migrate
================================================================================

1. Double-Click on the Quick launch icon named "QuickMigrate" on the Desktop. This will launch the tool.
2. Provide the Database details of the OpenManage Essentials in the field named "OM Essentials Database Server". The details should be provided in the format Database IP (or FQDN)/DB Instance Name. The default values are already populated if the OpenManage Essentials is installed with typical settings.
3. Provide the database name for OpenManage Essentials. The default values are already populated if the OpenManage Essentials is installed with typical settings.
4. Provide the authentication type and required credentials and click on "Connect". Please note that credentials are required only in case of SQL authentication.
5. Once the connection is successful, please click on the "Next button".
6. Provide the OM Enterprise IP/FQDN and credentials and click on "Connect".
7. Once the connection is successful, please click on "Next" button. Wait for the next page to load.
8. Under the SMTP settings, please provide the username and password. This is required only if you have configured these settings in OpenManage Essentials. 
9. Under the Proxy settings, please provide the username and password if the proxy requires authentication (else leave the credentials blank). This is required only if you have configured these settings in OpenManage Essentials.
10.Under the "Discovery ranges", if you have common credentials for all the device ranges (For example, Active directory), please provide them under common credentials settings and click on Apply. If you do not have common credentials, select the option "Provide individual credentials for discovery ranges".Click on the link below and it will launch a new wizard to provide individual credentials.

Note: 
1. For user's security the passwords in OpenManage Essentials are encrypted and hence cannot be migrated. Hence, a user needs to provide them again in the tool.
2. The wizard for providing credentials for individual ranges will show only those discovery ranges that are created in OpenManage Essentials with protocols like WSMAN, IPMI, SSH, REST. In case any ranges are created with SNMP, they will be automatically migrated without user's intervention.
3. The device ranges that are not supported in OpenManage Enterprise will be dropped and will not be migrated. For example, EMC Navisphere, MD Array, WMI etc.
 

--------------------------------------------------------------------------------
Copyright (c) 2019 Dell Inc. or its subsidiaries. 

All rights reserved.
 Dell, EMC, and other trademarks are trademarks of Dell Inc. or its subsidiaries. Other trademarks may be trademarks of their respective owners.