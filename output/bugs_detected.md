# Detected bugs (automated tests)

*Bugs recorded when tests catch application errors.*

---
## Bug – 2026-02-11 21:03:31
- **Test:** `test_register_forbidden_characters`
- **Summary:** Application showed 'internal error' page (errorpage.htm) instead of validation message on register form.
- **URL:** https://demowebshop.tricentis.com/errorpage.htm?aspxerrorpath=/register
- **Scenario:** First name contained forbidden characters (e.g. script tag); expected client-side validation.
