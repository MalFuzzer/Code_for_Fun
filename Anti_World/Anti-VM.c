/* Written by Uriel Kosayev */

int main(int argc, char **argv)
{
 
char lszValue[100];
   HKEY hKey;
   int i=0;
    RegOpenKeyEx (HKEY_LOCAL_MACHINE, "SYSTEM\\CurrentControlSet\\Services\\Disk\\Enum", 0L, KEY_READ , &hKey);
 
    RegQueryValue(hKey,"0",lszValue,sizeof(lszValue));
 
    printf("%s", lszValue);
    if (strstr(lszValue, "VMware"))
    {
        printf("VMware Detected");
    }
 
     RegCloseKey(hKey);
    return 0;
 
}