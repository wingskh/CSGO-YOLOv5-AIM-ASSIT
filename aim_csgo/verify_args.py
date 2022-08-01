import torch

def verify_args(args):    
    if args.use_cuda and torch.cuda.is_available() == False:
        # print("--use-cuda 無GPU環境，請改為False")
        exit(0)

    if args.thickness < 1 / args.resize_window:
        # print("--thickness 請注意參數要求！")
        exit(0)

    if not (0 < args.region[0] <= 1) and not (0 < args.region[1] <= 1):
        # print("--region 請輸入0~1的數！")
        exit(0)

    if args.lock_button not in ['left', 'middle', 'right', 'x1', 'x2']:
        # print("--lock-button 只支持鼠標按鍵:left, middle, right, x1, x2")
        exit(0)

    for i in args.lock_choice:
        if i not in args.lock_tag:
            # print("--lock-choice 請注意參數要求！")
            exit(0)

    buttons = []
    buttons.append(args.lock_button)
    