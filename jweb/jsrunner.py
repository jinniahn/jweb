def get_parser():
    import argparse
    parser = argparse.ArgumentParser(description='web runner')
    parser.add_argument('jsfile', type=argparse.FileType('r'), help='javascript to run')
    parser.add_argument('--url', help='url to go before running javascript')
    return parser


def main():
    args = get_parser().parse_args()

    from jweb import run_web    
    driver = run_web.WebClient()

    cmd = '''
    var ret = (function(){
        %s
    })();
    return ret;
    ''' % args.jsfile.read();
    ret = driver.run_js(cmd)
    print(ret)



if __name__ == '__main__':
    main()
