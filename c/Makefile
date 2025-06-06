# CryptoLion SDK Makefile
# ------------------------
# Builds the C SDK and Python bindings

# Configuration
# -------------
CC = gcc
CFLAGS = -fPIC -Wall -Wextra -O2
LDFLAGS = -shared
LIBS = -lcurl -lcjson

# Platform detection
UNAME_S := $(shell uname -s)
UNAME_M := $(shell uname -m)

# Platform-specific settings
# --------------------------
ifeq ($(UNAME_S),Linux)
	LIB_NAME = libcryptolion.so
	PLATFORM = linux
	INSTALL_DIR = /usr/local/lib
	PYTHON_LIB_DIR = python/cryptolion/libs
endif
ifeq ($(UNAME_S),Darwin)
	LIB_NAME = libcryptolion.dylib
	PLATFORM = darwin
	INSTALL_DIR = /usr/local/lib
	PYTHON_LIB_DIR = python/cryptolion/libs
	CFLAGS += -I/opt/homebrew/include
	LDFLAGS += -L/opt/homebrew/lib
endif
ifeq ($(OS),Windows_NT)
	LIB_NAME = cryptolion.dll
	PLATFORM = windows
	INSTALL_DIR = C:/CryptoLion/lib
	PYTHON_LIB_DIR = python/cryptolion/libs
	CC = x86_64-w64-mingw32-gcc
	LIBS += -lws2_32 -lwldap32
endif

# Cross-compilation targets
# -------------------------
TARGETS = linux-amd64 linux-arm64 darwin-amd64 darwin-arm64 windows-amd64

# Source files
# ------------
SRC_DIR = c
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)
OBJ_FILES = $(SRC_FILES:.c=.o)
HEADER_FILES = $(wildcard $(SRC_DIR)/*.h)

# Python package
# --------------
PYTHON_DIR = python
SETUP_FILE = $(PYTHON_DIR)/setup.py

# Build targets
# -------------
.PHONY: all build lib test install clean distclean package cross-compile

all: build

build: lib

lib: $(SRC_DIR)/$(LIB_NAME)

$(SRC_DIR)/$(LIB_NAME): $(OBJ_FILES)
	$(CC) $(LDFLAGS) -o $@ $^ $(LIBS)

$(SRC_DIR)/%.o: $(SRC_DIR)/%.c $(HEADER_FILES)
	$(CC) $(CFLAGS) -c $< -o $@

# Cross-compilation for all platforms
cross-compile: $(TARGETS)

linux-amd64:
	$(MAKE) lib CC=x86_64-linux-gnu-gcc PLATFORM=linux ARCH=amd64 LIB_NAME=libcryptolion.so

linux-arm64:
	$(MAKE) lib CC=aarch64-linux-gnu-gcc PLATFORM=linux ARCH=arm64 LIB_NAME=libcryptolion.so

darwin-amd64:
	$(MAKE) lib CC=x86_64-apple-darwin19-gcc PLATFORM=darwin ARCH=amd64 LIB_NAME=libcryptolion.dylib \
		CFLAGS="$(CFLAGS) -target x86_64-apple-macos10.15" \
		LDFLAGS="$(LDFLAGS) -target x86_64-apple-macos10.15"

darwin-arm64:
	$(MAKE) lib CC=aarch64-apple-darwin20-gcc PLATFORM=darwin ARCH=arm64 LIB_NAME=libcryptolion.dylib \
		CFLAGS="$(CFLAGS) -target arm64-apple-macos11" \
		LDFLAGS="$(LDFLAGS) -target arm64-apple-macos11"

windows-amd64:
	$(MAKE) lib CC=x86_64-w64-mingw32-gcc PLATFORM=windows ARCH=amd64 LIB_NAME=cryptolion.dll \
		LIBS="$(LIBS) -lws2_32 -lwldap32"

# Python package
package: cross-compile
	@echo "Preparing Python package..."
	@mkdir -p $(PYTHON_LIB_DIR)
	@cp c/libcryptolion.so $(PYTHON_LIB_DIR)/libcryptolion_linux_amd64.so
	@cp c/libcryptolion.so $(PYTHON_LIB_DIR)/libcryptolion_linux_arm64.so
	@cp c/libcryptolion.dylib $(PYTHON_LIB_DIR)/libcryptolion_darwin_amd64.dylib
	@cp c/libcryptolion.dylib $(PYTHON_LIB_DIR)/libcryptolion_darwin_arm64.dylib
	@cp c/cryptolion.dll $(PYTHON_LIB_DIR)/cryptolion_windows_amd64.dll
	@echo "Building Python package..."
	@cd $(PYTHON_DIR) && python setup.py sdist bdist_wheel

install: lib
	@echo "Installing library to $(INSTALL_DIR)"
	@mkdir -p $(INSTALL_DIR)
	@cp $(SRC_DIR)/$(LIB_NAME) $(INSTALL_DIR)
	@echo "Updating dynamic linker cache..."
	@ldconfig || true

# Test targets
test: build
	@echo "Running tests..."
	@cd tests && $(MAKE) test

# Cleanup
clean:
	@echo "Cleaning object files..."
	@rm -f $(OBJ_FILES)
	@rm -f $(SRC_DIR)/*.so $(SRC_DIR)/*.dylib $(SRC_DIR)/*.dll
	@cd tests && $(MAKE) clean

distclean: clean
	@echo "Cleaning Python build artifacts..."
	@rm -rf $(PYTHON_DIR)/build $(PYTHON_DIR)/dist $(PYTHON_DIR)/*.egg-info
	@rm -rf $(PYTHON_LIB_DIR)
