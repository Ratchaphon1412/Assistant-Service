from CoreLocation import CLLocationManager, kCLDistanceFilterNone, kCLLocationAccuracyThreeKilometers
from Foundation import NSRunLoop, NSDate, NSObject


class CoreLocationMacOS(NSObject):
    def init(self):
        self = super(CoreLocationMacOS, self).init()
        self.locationManager = CLLocationManager.alloc().init()
        self.locationManager.setDelegate_(self)
        self.locationManager.setDistanceFilter_(kCLDistanceFilterNone)
        self.locationManager.setDesiredAccuracy_(
            kCLLocationAccuracyThreeKilometers)
        self.locationManager.startUpdatingLocation()
        self.lat = None
        self.long = None
        return self

    def locationManager_didUpdateToLocation_fromLocation_(self, manager, newloc, oldloc):
        if oldloc is not None:
            print("OLD:", oldloc.description())
            self.lat = oldloc.coordinate().latitude
            self.long = oldloc.coordinate().longtitude
        else:
            print("OLD: <None>")
            self.lat = newloc.coordinate().latitude
            self.long = newloc.coordinate().longitude
            print(self.lat, self.long)

    def locationManager_didFailWithError_(self, manager, err):
        print("ERR:", err.description())

    def getCoreLocationMac(self):
        NSRunLoop.currentRunLoop().runUntilDate_(
            NSDate.dateWithTimeIntervalSinceNow_(10))
        return str(self.lat), str(self.long)
