#Atividade 04 - Alissa Garcia Moreira -

#Função que classifica o Prompt do Usuário: 

def classificar_prompt(prompt):
    
    prompt_lower = prompt.lower()

    if "por exemplo" in prompt_lower or "como exemplo" in prompt_lower:
        if prompt_lower.count("por exemplo") > 1 or prompt_lower.count("como exemplo") > 1:
            tecnica = "Few-Shot"
            raciocinio = "O prompt contém múltiplos exemplos, caracterizando Few-Shot."
        else:
            tecnica = "One-Shot"
            raciocinio = "O prompt contém um único exemplo, caracterizando One-Shot."
        
    elif "você é" in prompt_lower or "seja um" in prompt_lower or "aja como um" in prompt_lower or "me responda como um" in prompt_lower:
        tecnica = "Role Prompting"
        raciocinio = "O prompt define um papel ou função para o modelo assumir."
        
    elif "passo a passo" in prompt_lower:
        tecnica = "ReAct"
        raciocinio = "O prompt incentiva raciocínio estruturado passo a passo (ReAct)."
        
    else:
        tecnica = "Zero-Shot"
        raciocinio = "O prompt é uma pergunta direta sem exemplos ou instruções adicionais."

    print(f"Técnica utilizada: {tecnica}")
    print(f"Raciocinio: {raciocinio}")


prompt_usuario = input("Digite o seu prompt: ")
print(f"\nArgumento: \"{prompt_usuario}\"")
classificar_prompt(prompt_usuario)