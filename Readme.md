# Quick Start Guide - Odoo 18 Real Estate

Panduan cepat untuk mulai menggunakan sistem Real Estate Management dengan Docker.

## 🚀 Quick Start (5 Menit)

### 1. Start Services

```bash
cd /home/vrs/Intern/Nashta/odoo-dev
docker compose up -d
```

### 2. Buat Database

1. Buka browser: `http://localhost:8069`
2. Create Database:
   - Master Password: `admin`
   - Database Name: `odoo_db`
   - Email: `admin@example.com`
   - Password: `admin`
   - Language: `Indonesian`
   - Demo data: `☐` (Uncheck)
3. Klik "Create database"

### 3. Install Module Estate

1. Login ke Odoo
2. Pergi ke **Apps**
3. Klik **Update Apps List**
4. Hapus filter "Apps"
5. Cari **"Real Estate Management"**
6. Klik **Install**

### 4. Mulai Gunakan

1. Klik menu **Real Estate → Advertisements → Properties**
2. Klik **New** untuk tambah properti
3. Isi data dan **Save**

✅ **Done!** Sistem siap digunakan.

---

## 📋 Common Commands

### Start/Stop

```bash
# Start
docker compose up -d

#stop container
docker compose stop

# Stop and remove
docker compose down

# Restart
docker compose restart odoo18

# Logs
docker compose logs -f odoo18
```

### Update Module (Setelah Edit Code)

```bash
docker compose exec odoo18 odoo \
  -d odoo_db \
  -u estate \
  --db_host=db \
  --db_user=odoo \
  --db_password=odoo \
  --stop-after-init

docker compose restart odoo18
```

### Install Estate Account (Optional)

```bash
# Install account dulu
docker compose exec odoo18 odoo \
  -d odoo_db \
  -i account \
  --db_host=db \
  --db_user=odoo \
  --db_password=odoo \
  --stop-after-init

# Install estate_account
docker compose exec odoo18 odoo \
  -d odoo_db \
  -i estate_account \
  --db_host=db \
  --db_user=odoo \
  --db_password=odoo \
  --stop-after-init

docker compose restart odoo18
```

### Backup Database

```bash
# Backup
docker compose exec db pg_dump -U odoo odoo_db > backup_$(date +%Y%m%d).sql

# Restore
cat backup_20240101.sql | docker compose exec -T db psql -U odoo -d odoo_db
```

---

## 🆘 Troubleshooting Quick Fix

### Port Already Used

```bash
# Cek process
sudo lsof -i :8069

# Kill process
sudo kill -9 <PID>
```

### Module Not Found

```bash
# Check files
docker compose exec odoo18 ls -la /mnt/extra-addons/estate

# Update apps list via UI: Apps → Update Apps List
```

### Container Won't Start

```bash
# Check logs
docker compose logs db
docker compose logs odoo18

# Recreate containers
docker compose down
docker compose up -d
```

### Clean Restart (Nuclear Option - Data Hilang!)

```bash
docker compose down -v
docker volume prune -f
docker compose up -d
# Setup ulang dari awal
```

---

## 📚 Dokumentasi Lengkap

Lihat `README.md` untuk dokumentasi lengkap dengan:
- Penjelasan detail setiap fitur
- Development workflow
- Best practices
- Security configuration
- Dan banyak lagi...

---

## 🎯 URLs

- **Web Interface**: http://localhost:8069
- **Database**: localhost:5432
- **Login**: admin@example.com / admin

---

*Happy Coding! 🚀*
