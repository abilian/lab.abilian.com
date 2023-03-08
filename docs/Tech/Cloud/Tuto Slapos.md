#slapos

## Install master

Debian 10.

```
# wget https://deploy.erp5.net/slapos-master-standalone
# bash slapos-master-standalone
```

```
root@debian-4gb-hel1-1:~# erp5-show -s
Build successful, connect to:
  https://65.109.142.83
 with
  username: zope  password: mxUv5c3hrXjBc0P9
```

→ NO.

Mail config:
```
hostname slapos-node.abilian.com
vi /etc/hostname
hostname
vi /etc/postfix/main.cf
service postfix restart
apt install postfix
```

---

## Install node

- [x] 1.  [ ] I have an account on [Rapid.Space Panel](http://panel.rapid.space)
    -   To create an account, please follow [How To Create An Account On Rapid.Space](https://handbook.rapid.space/rapidspace-HowTo.Create.An.Account.On.Rapid.Space)
    -   If the contract is deactivated, please let me know
- [x] 2.  [ ] I have my target server prepared
- [x] 3.  [ ] I have installed Re6stnet on my target server
    -   Please follow [How To Use SDN For A Single Server](https://handbook.rapid.space/rapidspace-HowTo.Use.SDN.For.A.Single.Server) to install re6st
- [x] 1.  [ ] I have installed SlapOS node on my target server
    -   Please follow [How To Install SlapOS Node (Comp-123)](https://handbook.rapid.space/rapidspace-HowTo.Install.Slapos.Node.Comp.123) to install slapos node
- [x] 2.  [ ] Theia supplied on my target server
    -   Please follow [How To Supply A Software To A Specific Computer (Theia Runner)](https://handbook.rapid.space/rapidspace-HowTo.Supply.A.Software.To.A.Specific.Computer.Theia.Runner) to supply Theia 
- [x] 3.  [ ] Theia instanciated on my target server
    -   Please follow [How To Request A Theia Runner](https://handbook.rapid.space/rapidspace-HowTo.Request.A.Theia.Runner) to have your theia instance
- [ ] 4.  [ ] SlapOS SR to define software 

2.  [ ] Theia supplied on my target server
    -   Please follow [How To Supply A Software To A Specific Computer (Theia Runner)](https://handbook.rapid.space/rapidspace-HowTo.Supply.A.Software.To.A.Specific.Computer.Theia.Runner) to supply Theia 
3.  [ ] Theia instanciated on my target server
    -   Please follow [How To Request A Theia Runner](https://handbook.rapid.space/rapidspace-HowTo.Request.A.Theia.Runner) to have your theia instance
4.  [ ] SlapOS SR to define software 
    -   Refer to HTML5AS tutorial on [Rapid.Space Learning Track](https://handbook.rapid.space/rapidspace-Learning.Track) 
        -   from section: _Develop single instance profiles with Rapid.Space_ to _Test software release_

----

Token: 20221205-1E0E945

---

## TODO

https://handbook.rapid.space/user/rapidspace-HowTo.Deploy.Django.Stack.In.Theia
