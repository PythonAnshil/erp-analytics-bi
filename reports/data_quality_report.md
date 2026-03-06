# Data Quality Report

Generated at: 2026-03-06 02:51:58

## 1. Row Count Summary

| Check | Value |
|---|---:|
| Raw Customers | 500 |
| Raw Employees | 250 |
| Raw Projects | 2000 |
| Raw Invoices | 20000 |
| Raw Payments | 15000 |
| Raw Timesheets | 150000 |
| Clean Customers | 500 |
| Clean Projects | 2000 |
| Clean Invoices | 20000 |
| Clean Payments | 15000 |
| Clean Timesheets | 150000 |

## 2. Primary Key Uniqueness Checks

| Check | Value |
|---|---:|
| Duplicate Customer IDs | 0 |
| Duplicate Project IDs | 0 |
| Duplicate Invoice IDs | 0 |
| Duplicate Payment IDs | 0 |
| Duplicate Timesheet IDs | 0 |

## 3. Referential Integrity Checks

| Check | Value |
|---|---:|
| Orphan Projects → Customers | 0 |
| Orphan Invoices → Projects | 0 |
| Orphan Payments → Invoices | 0 |
| Orphan Timesheets → Employees | 0 |
| Orphan Timesheets → Projects | 0 |

## 4. Business Rule Checks

| Check | Value |
|---|---:|
| Invalid Timesheet Hours (Raw) | 0 |
| Invalid Timesheet Hours (Clean) | 0 |
| Overdue Invoices (Clean) | 12642 |

## 5. Financial Summary

| Check | Value |
|---|---:|
| Total Clean Invoice Amount | 515708831.16 |
| Total Clean Payment Amount | 393358388.82 |
| Payment Coverage Ratio | 0.7628 |

## 6. Notes

- Clean-layer row counts may be lower than raw counts due to filtering and relational validation.
- Duplicate and orphan counts should ideally be zero.
- Invalid clean timesheet hours should be zero after cleaning.
- Payment coverage ratio below 1.0 is acceptable because not all invoices are expected to be paid.
