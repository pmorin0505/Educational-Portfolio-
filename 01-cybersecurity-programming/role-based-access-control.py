"""
Cybersecurity Programming – Role-Based Access Control (RBAC) Project

This script demonstrates a simple role-based access control system using Python OOP principles.
It simulates how access badges control entry to secure zones and logs all access attempts.

Skills demonstrated:
- Object-oriented programming
- Access control logic (RBAC)
- Security auditing and logs
- Role-based permissions systems
"""

from datetime import datetime

# -----------------------------
# Parent Class: AccessBadge
# -----------------------------
class AccessBadge:
    def __init__(self, holder_name, level="employee", active=True):
        self.holder_name = holder_name
        self.level = level
        self.active = active
        self.access_log = []

    def check_access(self, zone):
        result = self._can_enter(zone)
        self._log_access(zone, result)
        return result

    def _log_access(self, zone, result):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = {
            "name": self.holder_name,
            "time": timestamp,
            "zone": zone,
            "allowed": result
        }

        self.access_log.append(log_entry)

        with open("badge_logs.txt", "a") as file:
            file.write(f"{self.holder_name},{timestamp},{zone},{result}\n")

    def show_log(self):
        for entry in self.access_log:
            print(f"{entry['name']}, {entry['time']}")

    def toggle_active(self):
        self.active = not self.active

    def set_level(self, level):
        self.level = level

    def get_level(self):
        return self.level

    def _can_enter(self, zone):
        if not self.active:
            return False

        if self.level == "admin":
            return True

        if self.level in ["employee", "staff"]:
            if zone in ["lobby", "lab"]:
                return True

        if self.level == "guest":
            if zone == "lobby":
                return True

        return False


# -----------------------------
# StaffBadge Child Class
# -----------------------------
class StaffBadge(AccessBadge):
    def __init__(self, holder_name, level="staff", active=True, department="General"):
        super().__init__(holder_name, level, active)
        self.department = department

    def _can_enter(self, zone):
        if zone == "server_room" and self.department == "IT":
            return True

        return super()._can_enter(zone)


# -----------------------------
# GuestBadge Child Class
# -----------------------------
class GuestBadge(AccessBadge):
    def __init__(self, holder_name, supervisor, active=True):
        super().__init__(holder_name, level="guest", active=active)
        self.supervisor = supervisor


# -----------------------------
# Demo
# -----------------------------
if __name__ == "__main__":

    print("---- Demo Example ----")
    badge = StaffBadge("Alice", department="IT")
    badge.check_access("lobby")
    badge.check_access("server_room")
    badge.check_access("lab")
    badge.show_log()

    print("\n---- StaffBadge HR Example ----")
    sofia = StaffBadge("Sofia", department="HR")
    print("Lobby:", sofia.check_access("lobby"))
    print("Server Room:", sofia.check_access("server_room"))
    print("Lab:", sofia.check_access("lab"))
    sofia.show_log()

    print("\n---- GuestBadge Example ----")
    justin = GuestBadge("Justin", "Merry")
    print("Lobby:", justin.check_access("lobby"))
    print("Server Room:", justin.check_access("server_room"))
    print("Lab:", justin.check_access("lab"))
    justin.show_log()
