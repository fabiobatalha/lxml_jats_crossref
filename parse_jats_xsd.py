# coding: utf-8
import os

from lxml import etree

print('parsing JATS')
schema_root = etree.parse('xsd/JATS-journalpublishing1.xsd')
schema = etree.XMLSchema(schema_root)

print('parsing crossref')
schema_root = etree.parse('xsd/crossref4.4.0.xsd')
schema = etree.XMLSchema(schema_root)
