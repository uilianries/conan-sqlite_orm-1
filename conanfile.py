#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, tools
import os


class sqlite_ormConan(ConanFile):
    name = "sqlite_orm"
    version = "20180118"
    commit_id = "8c2dc3ae937c31b715c49f0d9dae109f92af1661"
    url = "https://github.com/bincrafters/conan-sqlite_orm"
    homepage = "https://github.com/fnc12/sqlite_orm"
    author = "AlexandrePTJ <alpetitjean@gmail.com>"
    description = "SQLite ORM light header only library for modern C++."
    no_copy_source = True
    license = "https://github.com/fnc12/sqlite_orm/blob/master/LICENSE"
    exports = ["LICENSE.md"]

    requires = (
        "sqlite3/[~=3]@bincrafters/stable"
    )

    # Custom attributes for Bincrafters recipe conventions
    source_subfolder = "source_subfolder"

    def source(self):
        source_url = "https://github.com/fnc12/sqlite_orm"
        tools.get("{0}/archive/{1}.tar.gz".format(source_url, self.commit_id))
        extracted_dir = self.name + "-" + self.commit_id
        os.rename(extracted_dir, self.source_subfolder)

    def package(self):
        include_folder = os.path.join(self.source_subfolder, "include")
        self.copy(pattern="LICENSE", dst="license", src=self.source_subfolder)
        self.copy(pattern="*", dst="include", src=include_folder)

    def package_id(self):
        self.info.header_only()
