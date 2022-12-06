import pykeepass as pk

kp = pk.create_database('/transfer/ldap_manager/neuer_db_user.kdbx', password='test123', keyfile=None, transformed_key=None)

# create a new group
group1 = kp.add_group(kp.root_group, 'General')
group2 = kp.add_group(group1, 'BIL - Billing (apc0)')

# create a new entry
entry = kp.add_entry(group2, 'posinsbil01proapc1_mit Beschreibung', 'posinsbil01proapc1', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='Schufa', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc1')
entry = kp.add_entry(group2, 'posinsbil01proapc2_mit Beschreibung', 'posinsbil01proapc2', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='CG', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc2')
entry = kp.add_entry(group2, 'posinsbil01proapc3_mit Beschreibung', 'posinsbil01proapc3', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='DBA', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc3')
entry = kp.add_entry(group2, 'posinsbil01proapc4_mit Beschreibung', 'posinsbil01proapc4', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='niemand', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc4')
entry = kp.add_entry(group2, 'posinsbil01proapc5_mit Beschreibung', 'posinsbil01proapc5', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='Schufa', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc5')
entry = kp.add_entry(group2, 'posinsbil01proapc6_mit Beschreibung', 'posinsbil01proapc6', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='Schufa', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc6')
entry = kp.add_entry(group2, 'posinsbil01proapc7_mit Beschreibung', 'posinsbil01proapc7', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='Schufa', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc7')
entry = kp.add_entry(group2, 'posinsbil01proapc8_mit Beschreibung', 'posinsbil01proapc8', 'myPassw0rdXX', url='http://postgres-manager-der-noch-kommt.de', owner='Schufa', sr='SR123352', home='/home/hopsasa/tralala/posinsbil01proapc8')


# save database
kp.save()
