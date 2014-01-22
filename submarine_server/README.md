submarine_app.py is the driver app that invokes a SubmarineUDPServer object.  The SubmarineUDPServer object will consume a very simple three-token message that will fit in a single udp packet.  It will look like this:

```
[ forward vector | turn vector | vertical vector ]
```
ex:
```
1.0 0.0 0.0
```
Each vector is a floating point range from 0.0 to 1.0.  0.0 is a full stop for that "axis" and 1.0 is full throttle for the same axis.

Controller apps can then send messages that control the submarine.

