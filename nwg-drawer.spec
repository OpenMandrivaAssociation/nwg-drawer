%undefine _debugsource_packages
Name:           nwg-drawer
Version:        0.6.0
Release:        1
Summary:        Application drawer for wlroots-based Wayland compositors
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-drawer
Source:         https://github.com/nwg-piotr/nwg-drawer/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        godeps-for-nwg-drawer-%{version}.tar.xz
BuildRequires:  golang
BuildRequires:  compiler(go-compiler)
BuildRequires:  make
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Application drawer for wlroots-based Wayland compositors.

%prep
%autosetup -p1 -a1

%build
export GOPATH=$(pwd)/.godeps:$(pwd)/gopath
go build -o bin/%{name}

%install
export GOPATH=$(pwd)/.godeps:$(pwd)/gopath
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r desktop-directories %{buildroot}%{_datadir}/%{name}
cp -r img %{buildroot}%{_datadir}/%{name}
install -m644 drawer.css %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_bindir}
install -m755 bin/%{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
