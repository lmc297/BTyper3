#!/usr/bin/env python3

import collections
import datetime
import os
import shutil
import sys
import urllib.request
import xml.etree.ElementTree as etree

import setuptools
from setuptools.command.build_py import build_py as _build_py


class build_py(_build_py):
    """A modified `build_py` command to download data files.
    """

    def run(self):
        from pprint import pprint

        self.download_pubmlst(os.path.join(self.build_lib, "btyper3"))
        _build_py.run(self)

    def download_pubmlst(self, btyper3_path):

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("downloading most recent PubMLST database at {}".format(now))

        with urllib.request.urlopen("https://pubmlst.org/data/dbases.xml") as req:
            xml_path = os.path.join(btyper3_path, "seq_mlst_db", "pubmlst.xml")
            self.mkpath(os.path.dirname(xml_path))
            with open(xml_path, "wb") as dst:
                shutil.copyfileobj(req, dst)

        tree = etree.parse(xml_path)
        root = tree.getroot()
        species = collections.defaultdict(list)
        for parent in root.iter("species"):
            for child in parent.iter("url"):
                species[parent.text.strip()].append(child.text)

        for url in species["Bacillus cereus"]:
            if "alleles_fasta" in url:
                with urllib.request.urlopen(url) as req:
                    fas_path = os.path.join(btyper3_path, "seq_mlst_db", "mlst.fast")
                    with open(fas_path, "ab") as dst:
                        shutil.copyfileobj(req, dst)
            elif "profiles_csv" in url:
                with urllib.request.urlopen(url) as req:
                    txt_path = os.path.join(btyper3_path, "seq_mlst_db", "bcereus.txt")
                    self.mkpath(os.path.dirname(xml_path))
                    with open(txt_path, "wb") as dst:
                        shutil.copyfileobj(req, dst)

        print("finished downloading most recent PubMLST database")


setuptools.setup(cmdclass={"build_py": build_py})
