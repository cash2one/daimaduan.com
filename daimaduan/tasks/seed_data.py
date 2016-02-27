from fabric.decorators import task

from daimaduan.models.syntax import Syntax


ALL_SUPPORTTED_SYNTAX = (
    # ('brainfuck', 'Brainfuck'),
    # ('cirru', 'Cirru'),
    # ('nimrod', 'Nimrod'),
    ('bash', 'Bash'),
    # ('golo', 'Golo'),
    # ('css+django', 'CSS+Django/Jinja'),
    # ('cfm', 'Coldfusion HTML'),
    # ('lagda', 'Literate Agda'),
    # ('xtend', 'Xtend'),
    # ('powershell', 'PowerShell'),
    # ('limbo', 'Limbo'),
    # ('jags', 'JAGS'),
    # ('kal', 'Kal'),
    # ('dylan-console', 'Dylan session'),
    ('java', 'Java'),
    # ('nemerle', 'Nemerle'),
    # ('css+erb', 'CSS+Ruby'),
    # ('mysql', 'MySQL'),
    ('cpp', 'C++'),
    # ('cbmbas', 'CBM BASIC V2'),
    # ('xml+smarty', 'XML+Smarty'),
    # ('ahk', 'autohotkey'),
    # ('openedge', 'OpenEdge ABL'),
    # ('cmake', 'CMake'),
    # ('sp', 'SourcePawn'),
    # ('mako', 'Mako'),
    # ('css+mozpreproc', 'CSS+mozpreproc'),
    # ('js+myghty', 'JavaScript+Myghty'),
    # ('rsl', 'RSL'),
    # ('scaml', 'Scaml'),
    # ('maql', 'MAQL'),
    # ('as', 'ActionScript'),
    # ('squidconf', 'SquidConf'),
    # ('fan', 'Fantom'),
    # ('bbcode', 'BBCode'),
    # ('css+myghty', 'CSS+Myghty'),
    # ('mupad', 'MuPAD'),
    # ('xml+erb', 'XML+Ruby'),
    # ('kconfig', 'Kconfig'),
    # ('pytb', 'Python Traceback'),
    # ('cfs', 'cfstatement'),
    # ('ada', 'Ada'),
    # ('xul+mozpreproc', 'XUL+mozpreproc'),
    # ('css+mako', 'CSS+Mako'),
    # ('cucumber', 'Gherkin'),
    # ('io', 'Io'),
    # ('urbiscript', 'UrbiScript'),
    # ('plpgsql', 'PL/pgSQL'),
    # ('inform6', 'Inform 6'),
    # ('mozpercentpreproc', 'mozpercentpreproc'),
    # ('bro', 'Bro'),
    # ('antlr-objc', 'ANTLR With ObjectiveC Target'),
    ('xml', 'XML'),
    # ('nit', 'Nit'),
    # ('genshitext', 'Genshi Text'),
    # ('pike', 'Pike'),
    # ('objective-j', 'Objective-J'),
    # ('pycon', 'Python console session'),
    # ('ragel-c', 'Ragel in C Host'),
    # ('idl', 'IDL'),
    # ('aspx-cs', 'aspx-cs'),
    # ('ragel-ruby', 'Ragel in Ruby Host'),
    # ('html+genshi', 'HTML+Genshi'),
    ('spec', 'RPMSpec'),
    # ('css+smarty', 'CSS+Smarty'),
    # ('antlr-csharp', 'ANTLR With C# Target'),
    # ('llvm', 'LLVM'),
    # ('py3tb', 'Python 3.0 Traceback'),
    # ('ts', 'TypeScript'),
    # ('minid', 'MiniD'),
    ('sql', 'SQL'),
    ('json', 'JSON'),
    # ('nasm', 'NASM'),
    # ('idris', 'Idris'),
    # ('autoit', 'AutoIt'),
    ('sass', 'Sass'),
    # ('aspx-vb', 'aspx-vb'),
    # ('ceylon', 'Ceylon'),
    # ('html+evoque', 'HTML+Evoque'),
    # ('numpy', 'NumPy'),
    ('coffee-script', 'CoffeeScript'),
    # ('xml+mako', 'XML+Mako'),
    # ('css+php', 'CSS+PHP'),
    ('vim', 'VimL'),
    # ('css+genshitext', 'CSS+Genshi Text'),
    # ('fancy', 'Fancy'),
    # ('ragel', 'Ragel'),
    # ('ssp', 'Scalate Server Page'),
    # ('at', 'AmbientTalk'),
    # ('xml+evoque', 'XML+Evoque'),
    # ('redcode', 'Redcode'),
    # ('robotframework', 'RobotFramework'),
    ('scala', 'Scala'),
    # ('lighty', 'Lighttpd configuration file'),
    # ('rql', 'RQL'),
    # ('chapel', 'Chapel'),
    # ('html+velocity', 'HTML+Velocity'),
    # ('rbcon', 'Ruby irb session'),
    ('css', 'CSS'),
    # ('ragel-d', 'Ragel in D Host'),
    # ('asy', 'Asymptote'),
    # ('xml+php', 'XML+PHP'),
    # ('gnuplot', 'Gnuplot'),
    # ('pot', 'Gettext Catalog'),
    ('matlab', 'Matlab'),
    ('c', 'C'),
    # ('eiffel', 'Eiffel'),
    # ('genshi', 'Genshi'),
    # ('vgl', 'VGL'),
    # ('velocity', 'Velocity'),
    # ('koka', 'Koka'),
    # ('alloy', 'Alloy'),
    # ('irc', 'IRC logs'),
    # ('swig', 'SWIG'),
    # ('prolog', 'Prolog'),
    # ('xml+lasso', 'XML+Lasso'),
    # ('smalltalk', 'Smalltalk'),
    ('yaml', 'YAML'),
    # ('antlr-as', 'ANTLR With ActionScript Target'),
    # ('cypher', 'Cypher'),
    # ('xslt', 'XSLT'),
    # ('splus', 'S'),
    # ('dylan-lid', 'DylanLID'),
    # ('ec', 'eC'),
    # ('perl6', 'Perl6'),
    # ('logos', 'Logos'),
    # ('racket', 'Racket'),
    ('text', 'Text only'),
    ('dart', 'Dart'),
    # ('ragel-cpp', 'Ragel in CPP Host'),
    # ('scilab', 'Scilab'),
    # ('jsp', 'Java Server Page'),
    # ('abap', 'ABAP'),
    # ('rust', 'Rust'),
    ('diff', 'Diff'),
    # ('liquid', 'liquid'),
    # ('matlabsession', 'Matlab session'),
    # ('slim', 'Slim'),
    # ('html+php', 'HTML+PHP'),
    # ('objective-c++', 'Objective-C++'),
    # ('postscript', 'PostScript'),
    # ('verilog', 'verilog'),
    # ('js+erb', 'JavaScript+Ruby'),
    # ('cobolfree', 'COBOLFree'),
    # ('basemake', 'Base Makefile'),
    # ('ioke', 'Ioke'),
    # ('pypylog', 'PyPy Log'),
    # ('python3', 'Python 3'),
    ('swift', 'Swift'),
    # ('antlr', 'ANTLR'),
    # ('psql', 'PostgreSQL console (psql)'),
    # ('js+django', 'JavaScript+Django/Jinja'),
    # ('lsl', 'LSL'),
    # ('mathematica', 'Mathematica'),
    # ('erl', 'Erlang erl session'),
    # ('modelica', 'Modelica'),
    # ('antlr-python', 'ANTLR With Python Target'),
    # ('treetop', 'Treetop'),
    # ('tcl', 'Tcl'),
    # ('fsharp', 'FSharp'),
    # ('newlisp', 'NewLisp'),
    # ('css+lasso', 'CSS+Lasso'),
    # ('todotxt', 'Todotxt'),
    # ('shell-session', 'Shell Session'),
    # ('newspeak', 'Newspeak'),
    # ('console', 'Bash Session'),
    # ('gst', 'Gosu Template'),
    # ('tads3', 'TADS 3'),
    # ('rd', 'Rd'),
    # ('resource', 'ResourceBundle'),
    ('js', 'JavaScript'),
    # ('common-lisp', 'Common Lisp'),
    # ('apl', 'APL'),
    # ('gap', 'GAP'),
    # ('factor', 'Factor'),
    # ('awk', 'Awk'),
    # ('systemverilog', 'systemverilog'),
    # ('js+mako', 'JavaScript+Mako'),
    # ('iex', 'Elixir iex session'),
    # ('html+cheetah', 'HTML+Cheetah'),
    # ('i6t', 'Inform 6 template'),
    # ('julia', 'Julia'),
    # ('smarty', 'Smarty'),
    # ('protobuf', 'Protocol Buffer'),
    # ('tea', 'Tea'),
    # ('jasmin', 'Jasmin'),
    # ('apacheconf', 'ApacheConf'),
    # ('js+genshitext', 'JavaScript+Genshi Text'),
    # ('scheme', 'Scheme'),
    ('puppet', 'Puppet'),
    # ('octave', 'Octave'),
    # ('live-script', 'LiveScript'),
    # ('monkey', 'Monkey'),
    # ('red', 'Red'),
    # ('cfc', 'Coldfusion CFC'),
    # ('d-objdump', 'd-objdump'),
    # ('haxeml', 'Hxml'),
    ('groovy', 'Groovy/Gradle'),
    # ('jsonld', 'JSON-LD'),
    # ('pig', 'Pig'),
    # ('cuda', 'CUDA'),
    # ('handlebars', 'Handlebars'),
    # ('http', 'HTTP'),
    ('python', 'Python'),
    # ('boo', 'Boo'),
    # ('logtalk', 'Logtalk'),
    # ('vb.net', 'VB.net'),
    # ('d', 'D'),
    # ('blitzbasic', 'BlitzBasic'),
    ('scss', 'SCSS'),
    # ('haml', 'Haml'),
    # ('foxpro', 'FoxPro'),
    # ('control', 'Debian Control file'),
    # ('jade', 'Jade'),
    # ('c-objdump', 'c-objdump'),
    # ('xml+velocity', 'XML+Velocity'),
    # ('js+cheetah', 'JavaScript+Cheetah'),
    # ('cobol', 'COBOL'),
    # ('objdump', 'objdump'),
    # ('ca65', 'ca65 assembler'),
    # ('sparql', 'SPARQL'),
    # ('lasso', 'Lasso'),
    # ('ragel-java', 'Ragel in Java Host'),
    # ('vala', 'Vala'),
    # ('haskell', 'Haskell'),
    ('lua', 'Lua'),
    # ('aspectj', 'AspectJ'),
    # ('groff', 'Groff'),
    # ('js+lasso', 'JavaScript+Lasso'),
    # ('glsl', 'GLSL'),
    # ('gas', 'GAS'),
    # ('mxml', 'MXML'),
    # ('xml+cheetah', 'XML+Cheetah'),
    ('go', 'Go'),
    # ('pan', 'Pan'),
    # ('mql', 'MQL'),
    # ('felix', 'Felix'),
    # ('properties', 'Properties'),
    # ('igor', 'Igor'),
    # ('blitzmax', 'BlitzMax'),
    ('perl', 'Perl'),
    # ('stan', 'Stan'),
    ('ini', 'INI'),
    # ('rhtml', 'RHTML'),
    # ('coq', 'Coq'),
    # ('tcsh', 'Tcsh'),
    # ('dpatch', 'Darcs Patch'),
    # ('twig', 'Twig'),
    ('nginx', 'Nginx configuration file'),
    # ('agda', 'Agda'),
    # ('applescript', 'AppleScript'),
    # ('html+smarty', 'HTML+Smarty'),
    # ('inform7', 'Inform 7'),
    # ('lhs', 'Literate Haskell'),
    ('php', 'PHP'),
    # ('mscgen', 'Mscgen'),
    # ('ooc', 'Ooc'),
    # ('sourceslist', 'Debian Sourcelist'),
    # ('delphi', 'Delphi'),
    # ('modula2', 'Modula-2'),
    # ('postgresql', 'PostgreSQL SQL dialect'),
    # ('rexx', 'Rexx'),
    # ('html+django', 'HTML+Django/Jinja'),
    # ('hx', 'Haxe'),
    # ('django', 'Django/Jinja'),
    # ('dtd', 'DTD'),
    # ('nixos', 'Nix'),
    # ('vhdl', 'vhdl'),
    # ('mask', 'Mask'),
    # ('zephir', 'Zephir'),
    # ('pawn', 'Pawn'),
    # ('js+smarty', 'JavaScript+Smarty'),
    # ('html+twig', 'HTML+Twig'),
    # ('fortran', 'Fortran'),
    # ('cryptol', 'Cryptol'),
    # ('rebol', 'REBOL'),
    ('erb', 'ERB'),
    # ('befunge', 'Befunge'),
    # ('moon', 'MoonScript'),
    # ('dylan', 'Dylan'),
    # ('trac-wiki', 'MoinMoin/Trac Wiki markup'),
    # ('croc', 'Croc'),
    ('html', 'HTML'),
    ('rst', 'reStructuredText'),
    # ('nsis', 'NSIS'),
    # ('elixir', 'Elixir'),
    # ('isabelle', 'Isabelle'),
    # ('html+myghty', 'HTML+Myghty'),
    ('make', 'Makefile'),
    # ('sqlite3', 'sqlite3con'),
    # ('ocaml', 'OCaml'),
    # ('clay', 'Clay'),
    # ('jlcon', 'Julia console'),
    ('rb', 'Ruby'),
    # ('pov', 'POVRay'),
    # ('dg', 'dg'),
    # ('evoque', 'Evoque'),
    ('docker', 'Docker'),
    # ('registry', 'reg'),
    # ('html+mako', 'HTML+Mako'),
    # ('cfengine3', 'CFEngine3'),
    # ('mason', 'Mason'),
    # ('lean', 'Lean'),
    # ('lcry', 'Literate Cryptol'),
    # ('as3', 'ActionScript 3'),
    ('kotlin', 'Kotlin'),
    # ('antlr-java', 'ANTLR With Java Target'),
    # ('bugs', 'BUGS'),
    # ('javascript+mozpreproc', 'Javascript+mozpreproc'),
    # ('yaml+jinja', 'YAML+Jinja'),
    # ('cpp-objdump', 'cpp-objdump'),
    # ('bat', 'Batchfile'),
    # ('hybris', 'Hybris'),
    # ('opa', 'Opa'),
    # ('hylang', 'Hy'),
    # ('cython', 'Cython'),
    # ('erlang', 'Erlang'),
    # ('vctreestatus', 'VCTreeStatus'),
    ('clojure', 'Clojure'),
    # ('antlr-perl', 'ANTLR With Perl Target'),
    # ('mozhashpreproc', 'mozhashpreproc'),
    # ('myghty', 'Myghty'),
    # ('clojurescript', 'ClojureScript'),
    # ('qml', 'QML'),
    # ('moocode', 'MOOCode'),
    # ('rconsole', 'RConsole'),
    # ('raw', 'Raw token data'),
    # ('html+lasso', 'HTML+Lasso'),
    ('csharp', 'C#'),
    # ('tex', 'TeX'),
    # ('chai', 'ChaiScript'),
    # ('cheetah', 'Cheetah'),
    # ('smali', 'Smali'),
    # ('qbasic', 'QBasic'),
    # ('gooddata-cl', 'GoodData-CL'),
    # ('html+handlebars', 'HTML+Handlebars'),
    ('objective-c', 'Objective-C'),
    # ('lidr', 'Literate Idris'),
    # ('ragel-em', 'Embedded Ragel'),
    # ('objdump-nasm', 'objdump-nasm'),
    # ('antlr-cpp', 'ANTLR With CPP Target'),
    # ('ebnf', 'EBNF'),
    # ('gosu', 'Gosu'),
    # ('snobol', 'Snobol'),
    # ('js+php', 'JavaScript+PHP'),
    # ('xquery', 'XQuery'),
    # ('nesc', 'nesC'),
    # ('ecl', 'ECL'),
    # ('ragel-objc', 'Ragel in Objective C Host'),
    # ('xml+django', 'XML+Django/Jinja'),
    # ('sml', 'Standard ML'),
    # ('antlr-ruby', 'ANTLR With Ruby Target'),
    # ('duel', 'Duel'),
    # ('xml+myghty', 'XML+Myghty')
)


@task
def seed():
    """Seed syntax data in MongoDB"""
    def find_or_create_syntax(key, name):
        syntax = Syntax.objects(key=key).first()
        if syntax is None:
            print "Seeding syntax: %s" % key
            Syntax(key=key, name=name).save()

    for key, name in ALL_SUPPORTTED_SYNTAX:
        find_or_create_syntax(key, name)
