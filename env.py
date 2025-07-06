import os

print("Loaded env.py")


os.environ.setdefault(
    "DATABASE_URL",
    "postgresql://neondb_owner:npg_NGlfDh7Fnti0@ep-silent-wildflower-a257kwc1.eu-central-1.aws.neon.tech/pulse_drum_relay_29444")

os.environ.setdefault(
    "SECRET_KEY",
    "m5+)#d1h2*#6+)2f&6w#n8m-be311cjf7-01=3-=2yo$*e-_of"
)
