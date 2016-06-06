#!/usr/bin/env python

import sys

import cs

DEBUG = True


def log(msg):
    if DEBUG:
        print(msg)


def security_group(name):
    con = cs.CloudStack(**cs.read_config())
    log("Creating security group named '{}'".format(name))
    sg = con.createSecurityGroup(name=name)['securitygroup']
    # For standard SSH access
    log("Add rule for SSH tcp/22")
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=22,
                                      endport=22,
                                      securitygroupid=sg['id'])
    # For Docker marchine acess
    log("Add rule for docker access tcp/2376")
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=2376,
                                      endport=2376,
                                      securitygroupid=sg['id'])
    # For tomcat webapp access
    log("Add rule for tomcat access tcp/8080")
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=8080,
                                      endport=8080,
                                      securitygroupid=sg['id'])
    # For rancher OS
    log("Add rule for rancher OS udp/500, udp/4500, tcp/9345, tcp/9346")
    con.authorizeSecurityGroupIngress(protocol="UDP",
                                      cidrlist="0.0.0.0/0",
                                      startport=500,
                                      endport=500,
                                      securitygroupid=sg['id'])
    # For rancher OS
    con.authorizeSecurityGroupIngress(protocol="UDP",
                                      cidrlist="0.0.0.0/0",
                                      startport=4500,
                                      endport=4500,
                                      securitygroupid=sg['id'])
    # For Rancher OS UI
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=9345,
                                      endport=9345,
                                      securitygroupid=sg['id'])
    # For Rancher OS UI
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=9346,
                                      endport=9346,
                                      securitygroupid=sg['id'])
    # For OpenVPN
    log("Add rule for OpenVPN access tcp/1194")
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=1194,
                                      endport=1194,
                                      securitygroupid=sg['id'])
    # For OpenVPN ssh access to extract configuration
    log("Add rule for OpenVPN configuration access tcp/2222")
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=2222,
                                      endport=2222,
                                      securitygroupid=sg['id'])
    # For HTTPS access for rancher
    log("Add rule for HTTPS traffic tcp/443")
    con.authorizeSecurityGroupIngress(protocol="TCP",
                                      cidrlist="0.0.0.0/0",
                                      startport=443,
                                      endport=443,
                                      securitygroupid=sg['id'])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("You must provide a name for the security group")
    else:
        security_group(sys.argv[1])
