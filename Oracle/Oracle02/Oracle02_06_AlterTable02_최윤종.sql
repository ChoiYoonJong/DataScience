SQL> alter table membert01 rename column mem_addr to mem_address;

Table altered.

SQL> desc memberT01;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME                                                                                                                   VARCHAR2(20)
 MEM_ID                                                                                                                     VARCHAR2(20)
 MEM_PWD                                                                                                                    VARCHAR2(20)
 MEM_EMAIL                                                                                                                  VARCHAR2(30)
 MEM_PHONE                                                                                                                  VARCHAR2(20)
 MEM_ADDRESS                                                                                                                VARCHAR2(20)