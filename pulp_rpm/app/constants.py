from types import SimpleNamespace


RPM_PLUGIN_TYPES = SimpleNamespace(
    PACKAGE='rpm.package',
    ADVISORY='rpm.advisory'
)

RPM_PLUGIN_TYPE_CHOICE_MAP = {
    'package': RPM_PLUGIN_TYPES.PACKAGE,
    'advisory': RPM_PLUGIN_TYPES.ADVISORY
}

CHECKSUM_TYPES = SimpleNamespace(
    UNKNOWN='unknown',
    MD5='md5',
    SHA='sha1',  # compatibility nickname from original createrepo
    SHA1='sha1',
    SHA224='sha224',
    SHA256='sha256',
    SHA384='sha384',
    SHA512='sha512'
)

# The same as above, but in a format that choice fields can use
CHECKSUM_CHOICES = (
    (CHECKSUM_TYPES.UNKNOWN, CHECKSUM_TYPES.UNKNOWN),
    (CHECKSUM_TYPES.MD5, CHECKSUM_TYPES.MD5),
    (CHECKSUM_TYPES.SHA, CHECKSUM_TYPES.SHA),
    (CHECKSUM_TYPES.SHA1, CHECKSUM_TYPES.SHA1),
    (CHECKSUM_TYPES.SHA224, CHECKSUM_TYPES.SHA224),
    (CHECKSUM_TYPES.SHA256, CHECKSUM_TYPES.SHA256),
    (CHECKSUM_TYPES.SHA384, CHECKSUM_TYPES.SHA384),
    (CHECKSUM_TYPES.SHA512, CHECKSUM_TYPES.SHA512)
)

CR_PACKAGE_ATTRS = SimpleNamespace(
    ARCH='arch',
    CHANGELOGS='changelogs',
    CHECKSUM_TYPE='checksum_type',
    CONFLICTS='conflicts',
    DESCRIPTION='description',
    ENHANCES='enhances',
    EPOCH='epoch',
    FILES='files',
    LOCATION_BASE='location_base',
    LOCATION_HREF='location_href',
    NAME='name',
    OBSOLETES='obsoletes',
    PKGID='pkgId',
    PROVIDES='provides',
    RECOMMENDS='recommends',
    RELEASE='release',
    REQUIRES='requires',
    RPM_BUILDHOST='rpm_buildhost',
    RPM_GROUP='rpm_group',
    RPM_HEADER_END='rpm_header_end',
    RPM_HEADER_START='rpm_header_start',
    RPM_LICENSE='rpm_license',
    RPM_PACKAGER='rpm_packager',
    RPM_SOURCERPM='rpm_sourcerpm',
    RPM_VENDOR='rpm_vendor',
    SIZE_ARCHIVE='size_archive',
    SIZE_INSTALLED='size_installed',
    SIZE_PACKAGE='size_package',
    SUGGESTS='suggests',
    SUMMARY='summary',
    SUPPLEMENTS='supplements',
    TIME_BUILD='time_build',
    TIME_FILE='time_file',
    URL='url',
    VERSION='version'
)

PACKAGE_REPODATA = ['primary', 'filelists', 'other']
PACKAGE_DB_REPODATA = ['primary_db', 'filelists_db', 'other_db']
UPDATE_REPODATA = ['updateinfo']
MODULAR_REPODATA = ['modules']
COMPS_REPODATA = ['group']
SKIP_REPODATA = ['group_gz']

CR_UPDATE_RECORD_ATTRS = SimpleNamespace(
    ID='id',
    UPDATED_DATE='updated_date',
    DESCRIPTION='description',
    ISSUED_DATE='issued_date',
    FROMSTR='fromstr',
    STATUS='status',
    TITLE='title',
    SUMMARY='summary',
    VERSION='version',
    TYPE='type',
    SEVERITY='severity',
    SOLUTION='solution',
    RELEASE='release',
    RIGHTS='rights',
    PUSHCOUNT='pushcount'
)

CR_UPDATE_COLLECTION_ATTRS = SimpleNamespace(
    NAME='name',
    SHORTNAME='shortname',
    MODULE='module'
)

CR_UPDATE_COLLECTION_PACKAGE_ATTRS = SimpleNamespace(
    ARCH='arch',
    EPOCH='epoch',
    FILENAME='filename',
    NAME='name',
    REBOOT_SUGGESTED='reboot_suggested',
    RELEASE='release',
    SRC='src',
    SUM='sum',
    SUM_TYPE='sum_type',
    VERSION='version'
)

CR_UPDATE_REFERENCE_ATTRS = SimpleNamespace(
    HREF='href',
    ID='id',
    TITLE='title',
    TYPE='type'
)

CR_UPDATE_COLLECTION_ATTRS_MODULE = SimpleNamespace(
    NAME='name',
    STREAM='stream',
    VERSION='version',
    CONTEXT='context',
    ARCH='arch'
)

PULP_UPDATE_REFERENCE_ATTRS = SimpleNamespace(
    HREF='href',
    ID='ref_id',
    TITLE='title',
    TYPE='ref_type'
)

PULP_PACKAGE_ATTRS = CR_PACKAGE_ATTRS
PULP_UPDATE_RECORD_ATTRS = CR_UPDATE_RECORD_ATTRS
PULP_UPDATE_COLLECTION_ATTRS = CR_UPDATE_COLLECTION_ATTRS
PULP_UPDATE_COLLECTION_PACKAGE_ATTRS = CR_UPDATE_COLLECTION_PACKAGE_ATTRS

PULP_UPDATE_COLLECTION_ATTRS_MODULE = CR_UPDATE_COLLECTION_ATTRS_MODULE

MODULEMD_MODULE_ATTR = SimpleNamespace(
    ARCH='arch',
    ARTIFACTS='artifacts',
    CONTEXT='context',
    NAME='name',
    STREAM='stream',
    VERSION='version',
    DEPENDENCIES='dependencies'
)

MODULEMD_MODULEDEFAULTS_ATTR = SimpleNamespace(
    MODULE='module',
    STREAM='stream',
    PROFILES='profiles'
)

PULP_MODULEDEFAULTS_ATTR = SimpleNamespace(
    MODULE='module',
    STREAM='stream',
    PROFILES='profiles',
    DIGEST='digest'
)

PULP_MODULE_ATTR = MODULEMD_MODULE_ATTR

LIBCOMPS_GROUP_ATTRS = SimpleNamespace(
    ID='id',
    DEFAULT='default',
    USER_VISIBLE='uservisible',
    DISPLAY_ORDER='display_order',
    NAME='name',
    DESCRIPTION='desc',
    PACKAGES='packages',
    BIARCH_ONLY='biarchonly',
    DESC_BY_LANG='desc_by_lang',
    NAME_BY_LANG='name_by_lang'
)

LIBCOMPS_CATEGORY_ATTRS = SimpleNamespace(
    ID='id',
    NAME='name',
    DESCRIPTION='desc',
    DISPLAY_ORDER='display_order',
    GROUP_IDS='group_ids',
    DESC_BY_LANG='desc_by_lang',
    NAME_BY_LANG='name_by_lang'
)

LIBCOMPS_ENVIRONMENT_ATTRS = SimpleNamespace(
    ID='id',
    NAME='name',
    DESCRIPTION='desc',
    DISPLAY_ORDER='display_order',
    GROUP_IDS='group_ids',
    OPTION_IDS='option_ids',
    DESC_BY_LANG='desc_by_lang',
    NAME_BY_LANG='name_by_lang'
)

PULP_LANGPACKS_ATTRS = SimpleNamespace(
    MATCHES='matches'
)

PULP_GROUP_ATTRS = SimpleNamespace(
    ID='id',
    DEFAULT='default',
    USER_VISIBLE='user_visible',
    DISPLAY_ORDER='display_order',
    NAME='name',
    DESCRIPTION='description',
    PACKAGES='packages',
    BIARCH_ONLY='biarch_only',
    DESC_BY_LANG='desc_by_lang',
    NAME_BY_LANG='name_by_lang'
)

PULP_CATEGORY_ATTRS = SimpleNamespace(
    ID='id',
    NAME='name',
    DESCRIPTION='description',
    DISPLAY_ORDER='display_order',
    GROUP_IDS='group_ids',
    DESC_BY_LANG='desc_by_lang',
    NAME_BY_LANG='name_by_lang'
)

PULP_ENVIRONMENT_ATTRS = SimpleNamespace(
    ID='id',
    NAME='name',
    DESCRIPTION='description',
    DISPLAY_ORDER='display_order',
    GROUP_IDS='group_ids',
    OPTION_IDS='option_ids',
    DESC_BY_LANG='desc_by_lang',
    NAME_BY_LANG='name_by_lang'
)
